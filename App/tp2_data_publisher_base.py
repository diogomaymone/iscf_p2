import paho.mqtt.publish as pub
import numpy as np
import os
import time

def generate(median=90, err=10, outlier_err=30, size=1000, outlier_size=10):
    errs = err * np.random.rand(size) * np.random.choice((-1, 1), size)
    data = median + errs

    lower_errs = outlier_err * np.random.rand(outlier_size)
    lower_outliers = median - err - lower_errs

    upper_errs = outlier_err * np.random.rand(outlier_size)
    upper_outliers = median + err + upper_errs

    data = np.concatenate((data, lower_outliers, upper_outliers))
    np.random.shuffle(data)

    return data

if __name__ == '__main__':
    broker = os.environ.get('MQTT_BROKER')
    rate = float(os.environ.get('PUBLISH_RATE'))
    topic = os.environ.get('MQTT_TOPIC')

    data = generate()

    while True:
        value = np.random.choice(data)
        if np.random.rand() < 0.1:
            value = None

        if value is not None:
            pub.single(topic, value, hostname=broker)
            print(f"Published value: {value}")

        time.sleep(rate)
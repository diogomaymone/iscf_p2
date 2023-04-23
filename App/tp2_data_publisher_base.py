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
    # retrieve the environment variable values for the mqtt broker and the desired rate for the publisher
    broker = os.environ.get('MQTT_BROKER')
    rate = float(os.environ.get('PUBLISH_RATE'))
    topic = os.environ.get('MQTT_TOPIC')

    # use the generate function to create a pool of values for the publisher
    data = generate()

    # publish a msg with a value randomly sampled from the data array.
    # make it so that there's a 10% chance the value sent is null to emulate a sensor failure
    # you should filter these null values in Node Red
    while True:
        value = np.random.choice(data)
        if np.random.rand() < 0.1:
            value = None
        if value is not None:
            payload = str(value)
            pub.single(topic, payload=payload, hostname=broker)
        time.sleep(1/rate)
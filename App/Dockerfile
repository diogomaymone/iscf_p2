FROM python:3.9

RUN pip install paho-mqtt numpy

COPY . /app
WORKDIR /app

CMD ["python", "tp2_data_publisher_base.py"]
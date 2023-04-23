FROM python:3.9

WORKDIR /app

RUN pip install paho-mqtt numpy

COPY . .

CMD ["python", "./tp2_data_publisher_base.py"]
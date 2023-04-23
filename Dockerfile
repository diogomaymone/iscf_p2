FROM python:3.9

WORKDIR /P2

RUN pip install paho-mqtt

COPY . .

CMD ["python", "tp2_data_publisher_base.py"]

EXPOSE 3000
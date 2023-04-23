# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install paho-mqtt numpy

# Define environment variables
ENV BROKER ""
ENV RATE ""
ENV TOPIC ""

# Run app.py when the container launches
CMD ["python", "tp2_data_publisher_base.py"]

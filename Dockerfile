
FROM ubuntu:20.04

# Stage 1: Install OpenJDK
FROM bitnami/spark:3.5.1

# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /lat_code

# Copy the current directory contents into the container at /app
COPY . /lat_code

# # Custom logging
# COPY log4j2.properties /opt/bitnami/spark/conf/log4j2.properties

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /lat_code/requirements.txt



# Install OpenJDK 11
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
# ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# # Verify installation
# RUN java -version

# Define environment variable
ENV SPARK_HOME /usr/local/lib/python3.12/site-packages/pyspark

# Make port 4040 available to the world outside this container (for Spark UI)
EXPOSE 4040

# # Run app.py when the container launches
# CMD ["python", "/lat_code/run.py"]

# Ensure the start script is executable
RUN chmod +x start.sh

# Run the start script when the container launches
CMD ["./start.sh"]


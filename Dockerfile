# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /python-docker

# Copy the requirements file into the container
# COPY requirements.txt requirements.txt
COPY requirements.txt ./

# Install any dependencies
RUN pip install -r requirements.txt
# RUN pip install -r 

# Copy the rest of the application code into the container
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# TODO: Define environment variable
ENV FLASK_APP=main.py

# Run the application
# TODO: si if I need flask cmd or just python, also that host arg I think is dangerous
CMD ["flask", "run", "--host=0.0.0.0"]

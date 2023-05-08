# Use an official Python runtime as the base image
FROM --platform=linux/amd64 python:3.9 as base

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the command to run when the container starts
CMD ["python", "app.py"]

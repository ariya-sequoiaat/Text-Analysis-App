# Use official Python base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command
CMD ["python", "appl_project/sync_data.py"]

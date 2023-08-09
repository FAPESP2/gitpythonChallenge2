
FROM python:3.9-slim

# directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8080 available
EXPOSE 8080

# Flask app when the container launches
CMD ["python", "app.py"]

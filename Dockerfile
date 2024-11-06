# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 for Flask app
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=flask_testing/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV OPENAI_API_KEY="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"


# Run the Flask app
CMD ["flask", "run"]

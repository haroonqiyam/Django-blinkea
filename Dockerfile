# Use Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create media directory
RUN mkdir -p /app/media

# Copy project
COPY . .

# Make start script executable
RUN chmod +x start.sh

# Create volume for media files
VOLUME /app/media

# Run start script which handles migrations and starts gunicorn
CMD ["./start.sh"]

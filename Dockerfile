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
    python3-dev \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    wget \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Create necessary directories
RUN mkdir -p /app/media /app/static /app/staticfiles

# Copy project
COPY . .

# Set proper permissions
RUN chmod +x start.sh && \
    chown -R www-data:www-data /app

# Switch to non-root user
USER www-data

# Create volume for media files
VOLUME /app/media

# Run start script which handles migrations and starts gunicorn
CMD ["bash", "-c", "echo \"Starting application on port $PORT\" && ./start.sh"]

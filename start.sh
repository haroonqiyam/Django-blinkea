#!/bin/bash

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p media
mkdir -p static

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser
echo "Creating superuser if not exists..."
python manage.py shell < create_superuser.py

# Load initial data if database is empty
echo "Checking and loading initial data if needed..."
python manage.py loaddata data.json

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run compress
echo "Compressing static files..."
python manage.py compress --force

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn --bind :$PORT blinkea.wsgi:application

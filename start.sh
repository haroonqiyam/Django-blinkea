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

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! pg_isready -h db -p 5432 -U blinkea_user; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn --bind :$PORT --workers 2 --threads 8 --timeout 0 blinkea.wsgi:application

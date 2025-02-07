#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Load initial data if database is empty
echo "Checking and loading initial data if needed..."
python manage.py loaddata data.json

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn --bind :$PORT blinkea.wsgi:application

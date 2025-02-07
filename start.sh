#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn --bind :$PORT blinkea.wsgi:application

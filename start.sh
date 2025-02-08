#!/bin/bash
set -e

echo "Starting Blinkea application..."

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p media static staticfiles

# Collect static files first (this doesn't require database)
echo "Collecting static files..."
python manage.py collectstatic --noinput || echo "Static collection failed but continuing..."

# Compress static files if compression is configured
if python manage.py help | grep -q compress; then
    echo "Compressing static files..."
    python manage.py compress --force || echo "Compression failed but continuing..."
fi

# Extract database connection info from DATABASE_URL
if [ -n "$DATABASE_URL" ]; then
    # Parse DATABASE_URL
    DB_USER=$(echo $DATABASE_URL | sed -n 's/postgres:\/\/\([^:]*\):.*/\1/p')
    DB_HOST=$(echo $DATABASE_URL | sed -n 's/.*@\([^:\/]*\).*/\1/p')
    DB_PORT=5432
    echo "Database configuration: host=$DB_HOST port=$DB_PORT user=$DB_USER"
else
    echo "WARNING: DATABASE_URL not set"
    DB_HOST="localhost"
    DB_PORT=5432
    DB_USER="postgres"
fi

# Wait for PostgreSQL with timeout
echo "Checking PostgreSQL connection on $DB_HOST:$DB_PORT..."
TIMEOUT=30
while ! pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -t 1 >/dev/null 2>&1; do
    TIMEOUT=$((TIMEOUT - 1))
    if [ $TIMEOUT -eq 0 ]; then
        echo "Timed out waiting for PostgreSQL to start"
        break
    fi
    echo "Waiting for PostgreSQL to start... ($TIMEOUT seconds left)"
    sleep 1
done

# Apply migrations (don't fail if they fail)
echo "Applying database migrations..."
python manage.py migrate --noinput || echo "Migrations failed but continuing..."

# Start Gunicorn with proper error handling
echo "Starting Gunicorn on port $PORT..."
exec gunicorn --bind :$PORT \
    --workers 2 \
    --threads 8 \
    --timeout 0 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    --capture-output \
    blinkea.wsgi:application

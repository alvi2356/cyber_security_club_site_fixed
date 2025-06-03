#!/usr/bin/env bash

# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z $PGHOST $PGPORT; do
  sleep 0.1
done
echo "Database is ready!"

# Run migrations again to ensure they're up to date
echo "Running migrations..."
python manage.py migrate --no-input

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn cyber_security_club_site.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --threads 8 --timeout 0 --access-logfile - --error-logfile - --log-level info 
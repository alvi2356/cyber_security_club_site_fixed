#!/usr/bin/env bash
# exit on error
set -o errexit

# Print Python version
python --version

# Print pip version
pip --version

# Install Python dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Print installed packages
echo "Installed packages:"
pip list

# Create static directory if it doesn't exist
mkdir -p static
mkdir -p staticfiles

# Remove old static files
echo "Cleaning old static files..."
rm -rf staticfiles/*

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

# Verify static files
echo "Verifying static files..."
python verify_static.py

# Run migrations
echo "Running migrations..."
python manage.py migrate --no-input

# Print environment variables (excluding sensitive ones)
echo "Environment variables:"
env | grep -v "SECRET" | grep -v "PASSWORD" | grep -v "KEY"

# Print database configuration
echo "Database configuration:"
python -c "from django.conf import settings; print('Database:', settings.DATABASES['default']['ENGINE'])"

# Print static files configuration
echo "Static files configuration:"
python -c "from django.conf import settings; print('STATIC_ROOT:', settings.STATIC_ROOT); print('STATIC_URL:', settings.STATIC_URL); print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)"

# List collected static files
echo "Listing collected static files:"
ls -R staticfiles/ 
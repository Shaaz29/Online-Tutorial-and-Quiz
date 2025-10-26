#!/usr/bin/env bash
# Build script for Render deployment

set -e  # Exit on error

echo "Building application..."

# Upgrade pip first
pip install --upgrade pip setuptools wheel

# Install psycopg2-binary explicitly first
pip install psycopg2-binary==2.9.9

# Install other dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput

echo "Build completed successfully!"


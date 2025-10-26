#!/usr/bin/env bash
# Build script for Render deployment

set -e  # Exit on error

echo "Building application..."

# Debug: Show Python version
echo "Python version:"
python --version

# Debug: Show pip version
echo "Pip version:"
pip --version

# Upgrade pip first
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel

# Install psycopg3 (works with Python 3.13)
echo "Installing psycopg for PostgreSQL..."
pip install "psycopg[binary]==3.2.12"

# Debug: Verify psycopg installation
echo "Checking psycopg installation:"
python -c "import psycopg; print('psycopg version:', psycopg.__version__)" || echo "Failed to import psycopg"

# Install other dependencies
echo "Installing other dependencies..."
pip install -r requirements.txt

# Debug: List installed packages
echo "Installed packages:"
pip list | grep -i psycopg

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

echo "Build completed successfully!"


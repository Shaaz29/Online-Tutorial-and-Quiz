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

# Install psycopg2-binary explicitly first
echo "Installing psycopg2-binary..."
pip install psycopg2-binary==2.9.9

# Debug: Verify psycopg2 installation
echo "Checking psycopg2 installation:"
python -c "import psycopg2; print('psycopg2 version:', psycopg2.__version__)" || echo "Failed to import psycopg2"

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


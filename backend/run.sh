#!/bin/sh

# Source environment variables from .env.prod
#. .env.prod

# Apply database migrations
echo "Applying database migrations"
python manage.py makemigrations --merge --noinput
python manage.py migrate

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --no-input

# Delay execution for 2 minutes
echo "Waiting for 2 minutes..."
sleep 120


# Start server
echo "Starting server"
python manage.py runserver
exec "$@"

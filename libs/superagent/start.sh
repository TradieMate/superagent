#!/bin/bash

# Exit on any error
set -e

echo "Starting Superagent API..."
echo "PORT: ${PORT:-8080}"
echo "Environment: ${NODE_ENV:-production}"

# Run database migrations if needed
echo "Running database migrations..."
prisma migrate deploy || echo "Migration failed or not needed"

# Generate Prisma client
echo "Generating Prisma client..."
prisma generate

# Start the application with proper binding
echo "Starting Gunicorn server..."
exec gunicorn \
    --bind 0.0.0.0:${PORT:-8080} \
    --workers ${WORKERS:-2} \
    --timeout ${TIMEOUT:-120} \
    --worker-class uvicorn.workers.UvicornWorker \
    --threads ${THREADS:-8} \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    app.main:app
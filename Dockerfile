# Use a Node.js base image for building frontend assets
FROM node:14 AS frontend-build

# Set working directory for the frontend
WORKDIR /app/frontend

# Copy frontend source code
COPY frontend/ .

# Install frontend dependencies
RUN npm install

# Build frontend assets
RUN npm run build

# Use a Python base image for running the application
FROM python:3.9-slim-buster AS backend

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    awscli

# Set working directory for the backend
WORKDIR /app/backend

# Copy backend source code
COPY backend/ .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy built frontend assets from frontend-build stage
COPY --from=frontend-build /app/frontend/build /app/backend/static

# Expose port (if applicable)
# EXPOSE 5000

# Set environment variables (if needed)
# ENV MY_VARIABLE=value

# Run the application
CMD ["python3", "app.py"]

# Base image for Python (backend)
FROM python:3.10-slim AS backend

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy backend dependencies
COPY ./backend/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY ./backend /app

# Expose backend port
EXPOSE 8000

# Command to run the FastAPI backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# ---------------------------------
# Frontend Stage
# ---------------------------------
FROM node:14 AS frontend

# Set working directory
WORKDIR /frontend

# Copy frontend dependencies
COPY ./frontend/package.json /frontend/package.json
COPY ./frontend/package-lock.json /frontend/package-lock.json

# Install Node.js dependencies
RUN npm install

# Copy frontend code
COPY ./frontend /frontend

# Build the frontend
RUN npm run build

# ---------------------------------
# Final Image
# ---------------------------------
FROM nginx:alpine

# Copy frontend build to Nginx directory
COPY --from=frontend /frontend/build /usr/share/nginx/html

# Expose frontend port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

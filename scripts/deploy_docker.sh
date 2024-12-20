#!/bin/bash

echo "Building Docker containers..."
docker-compose down
docker-compose build
docker-compose up -d
echo "Docker containers deployed successfully."

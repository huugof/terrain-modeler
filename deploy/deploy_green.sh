#!/usr/bin/env bash
set -euo pipefail

APP_IMAGE="${1:-${APP_IMAGE:-va-lidar-context:latest}}"

echo "Starting green deployment with image: ${APP_IMAGE}"
APP_IMAGE="${APP_IMAGE}" docker compose -f docker-compose.prod.yml --profile green up -d terrain-ui-green

echo "Waiting for green health..."
for i in {1..30}; do
  if docker compose -f docker-compose.prod.yml exec -T terrain-ui-green curl -fsS http://127.0.0.1:8000/healthz >/dev/null; then
    echo "Green is healthy."
    exit 0
  fi
  sleep 2
done

echo "Green failed health checks."
exit 1

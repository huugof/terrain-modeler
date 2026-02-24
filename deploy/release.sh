#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

APP_IMAGE="${1:-${APP_IMAGE:-}}"
SERVICE="terrain-ui"

./deploy/preflight.sh

echo "Deploying single-service stack (${SERVICE})..."
if [[ -n "${APP_IMAGE}" ]]; then
  echo "Image tag: ${APP_IMAGE}"
  APP_IMAGE="${APP_IMAGE}" docker compose up -d --build --remove-orphans "${SERVICE}" caddy
else
  docker compose up -d --build --remove-orphans "${SERVICE}" caddy
fi

# Ensure Caddy applies any changed Caddyfile immediately.
docker compose exec -T caddy caddy reload --config /etc/caddy/Caddyfile

echo "Waiting for ${SERVICE} health..."
for i in {1..30}; do
  if docker compose exec -T "${SERVICE}" curl -fsS http://127.0.0.1:8000/healthz >/dev/null; then
    echo "Deploy complete."
    exit 0
  fi
  sleep 2
done

echo "Health checks failed for ${SERVICE}." >&2
exit 1

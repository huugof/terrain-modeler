#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

APP_IMAGE="${1:-${APP_IMAGE:-}}"
CADDY_FILE="deploy/Caddyfile"

if [[ ! -f "${CADDY_FILE}" ]]; then
  echo "Missing ${CADDY_FILE}" >&2
  exit 1
fi

active="$(
  sed -n 's/.*reverse_proxy terrain-ui-\(blue\|green\):8000.*/\1/p' "${CADDY_FILE}" | head -n1
)"

if [[ "${active}" != "blue" && "${active}" != "green" ]]; then
  echo "Could not determine active color from ${CADDY_FILE}." >&2
  exit 1
fi

if [[ "${active}" == "blue" ]]; then
  target="green"
else
  target="blue"
fi

service="terrain-ui-${target}"

./deploy/preflight.sh

echo "Active traffic: ${active}"
echo "Deploy target: ${target}"
if [[ -n "${APP_IMAGE}" ]]; then
  echo "Image: ${APP_IMAGE}"
fi

if [[ "${target}" == "green" ]]; then
  if [[ -n "${APP_IMAGE}" ]]; then
    APP_IMAGE="${APP_IMAGE}" docker compose --profile green up -d "${service}"
  else
    docker compose --profile green up -d "${service}"
  fi
else
  if [[ -n "${APP_IMAGE}" ]]; then
    APP_IMAGE="${APP_IMAGE}" docker compose up -d "${service}"
  else
    docker compose up -d "${service}"
  fi
fi

echo "Waiting for ${service} health..."
for i in {1..30}; do
  if docker compose exec -T "${service}" curl -fsS http://127.0.0.1:8000/healthz >/dev/null; then
    ./deploy/switch_traffic.sh "${target}"
    echo "Release complete."
    echo "Rollback: ./deploy/switch_traffic.sh ${active}"
    exit 0
  fi
  sleep 2
done

echo "Health checks failed for ${service}; traffic remains on ${active}." >&2
exit 1

#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
if [[ "${TARGET}" != "blue" && "${TARGET}" != "green" ]]; then
  echo "Usage: $0 <blue|green>"
  exit 1
fi

CADDY_FILE="deploy/Caddyfile"
if [[ ! -f "${CADDY_FILE}" ]]; then
  echo "Missing ${CADDY_FILE}"
  exit 1
fi

if [[ "${TARGET}" == "blue" ]]; then
  sed -i.bak 's/reverse_proxy terrain-ui-green:8000/reverse_proxy terrain-ui-blue:8000/g' "${CADDY_FILE}"
else
  sed -i.bak 's/reverse_proxy terrain-ui-blue:8000/reverse_proxy terrain-ui-green:8000/g' "${CADDY_FILE}"
fi
rm -f "${CADDY_FILE}.bak"

docker compose -f docker-compose.prod.yml exec -T caddy caddy reload --config /etc/caddy/Caddyfile
echo "Traffic switched to ${TARGET}."

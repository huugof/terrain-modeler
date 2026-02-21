#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

if [[ ! -f .env ]]; then
  echo "Missing .env. Copy .env.example and set required values." >&2
  exit 1
fi

set -a
# shellcheck disable=SC1091
source .env
set +a

required_vars=(APP_DOMAIN ACME_EMAIL VA_SESSION_SECRET)
missing_vars=()
for var in "${required_vars[@]}"; do
  if [[ -z "${!var:-}" ]]; then
    missing_vars+=("${var}")
  fi
done

if (( ${#missing_vars[@]} > 0 )); then
  echo "Missing required .env values: ${missing_vars[*]}" >&2
  exit 1
fi

if [[ "${APP_DOMAIN}" == "example.com" || "${APP_DOMAIN}" == "your.domain.com" ]]; then
  echo "APP_DOMAIN looks like a placeholder: ${APP_DOMAIN}" >&2
  exit 1
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "docker is not installed or not in PATH." >&2
  exit 1
fi

docker compose config >/dev/null

a_records=""
if command -v dig >/dev/null 2>&1; then
  a_records="$(dig +short "${APP_DOMAIN}" A || true)"
  if [[ -z "${a_records}" ]]; then
    echo "WARNING: ${APP_DOMAIN} has no public A record yet."
  else
    echo "A records for ${APP_DOMAIN}:"
    echo "${a_records}"
  fi
fi

if command -v curl >/dev/null 2>&1; then
  public_ip="$(curl -fsS --max-time 5 https://api.ipify.org || true)"
  if [[ -n "${public_ip}" && -n "${a_records}" ]] && ! grep -Fxq "${public_ip}" <<<"${a_records}"; then
    echo "WARNING: Domain A record does not currently match this host's public IP (${public_ip})."
  fi
fi

echo "Preflight OK: compose config valid, required env vars set."

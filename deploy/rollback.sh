#!/usr/bin/env bash
set -euo pipefail

./deploy/switch_traffic.sh blue
echo "Rollback complete. Traffic points to blue."

#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"
BINARY_DIR="$ROOT_DIR/desktop/src-tauri/binaries"
SPEC_FILE="$ROOT_DIR/desktop/terrain-modeler.spec"
if [[ -n "${PYTHON_BIN:-}" ]]; then
  PYTHON_CMD="$PYTHON_BIN"
elif [[ -x "$ROOT_DIR/.venv/bin/python" ]]; then
  PYTHON_CMD="$ROOT_DIR/.venv/bin/python"
else
  PYTHON_CMD="python3"
fi

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "This script currently targets macOS sidecar builds only." >&2
  exit 1
fi

case "$(uname -m)" in
  arm64)
    TARGET_TRIPLE="aarch64-apple-darwin"
    ;;
  x86_64)
    TARGET_TRIPLE="x86_64-apple-darwin"
    ;;
  *)
    echo "Unsupported macOS architecture: $(uname -m)" >&2
    exit 1
    ;;
esac

cd "$ROOT_DIR"

"$PYTHON_CMD" -m pip install -e ".[dev]"
"$PYTHON_CMD" -m PyInstaller "$SPEC_FILE" --noconfirm --clean

mkdir -p "$BINARY_DIR"
cp "$DIST_DIR/terrain-modeler-backend" "$BINARY_DIR/terrain-modeler-backend"
cp "$DIST_DIR/terrain-modeler-backend" "$BINARY_DIR/terrain-modeler-backend-${TARGET_TRIPLE}"
chmod +x "$BINARY_DIR/terrain-modeler-backend" "$BINARY_DIR/terrain-modeler-backend-${TARGET_TRIPLE}"

echo "Built sidecar binaries:"
echo "  $BINARY_DIR/terrain-modeler-backend"
echo "  $BINARY_DIR/terrain-modeler-backend-${TARGET_TRIPLE}"

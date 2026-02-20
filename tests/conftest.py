import os
import sys
from pathlib import Path

# Ensure src/ is on sys.path for local test runs without installation.
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

# Provide a stable session secret so the module-level create_app() call in
# webapp/__init__.py succeeds in server mode without a real VA_SESSION_SECRET.
os.environ.setdefault("VA_SESSION_SECRET", "test-only-insecure-secret-do-not-use")

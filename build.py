"""
Build the website into static files in dist/ for free hosting on GitHub Pages.

    python build.py

GitHub Actions runs this automatically on every push (see .github/workflows/deploy.yml).
"""

import shutil
from pathlib import Path

from app import app

ROOT = Path(__file__).parent
DIST = ROOT / "dist"


def build() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    with app.test_client() as client:
        response = client.get("/")
        if response.status_code != 200:
            raise SystemExit(f"Rendering failed with status {response.status_code}")
        (DIST / "index.html").write_bytes(response.data)

    shutil.copytree(ROOT / "static", DIST / "static")
    (DIST / ".nojekyll").touch()  # tell GitHub Pages to serve files as-is
    print(f"Built site into {DIST}")


if __name__ == "__main__":
    build()

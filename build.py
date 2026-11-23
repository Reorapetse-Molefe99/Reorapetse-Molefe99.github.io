"""
Build the website into static files in dist/ for free hosting on GitHub Pages.

    python build.py

GitHub Actions runs this automatically on every push (see .github/workflows/deploy.yml).
"""

import shutil
from pathlib import Path

from app import app, credit_risk_routes

ROOT = Path(__file__).parent
DIST = ROOT / "dist"


def build() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    with app.test_client() as client:
        for route in ["/", *credit_risk_routes()]:
            response = client.get(route)
            if response.status_code != 200:
                raise SystemExit(f"Rendering {route} failed with status {response.status_code}")
            out = DIST / route.lstrip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(response.data)

    shutil.copytree(ROOT / "static", DIST / "static")
    (DIST / ".nojekyll").touch()  # tell GitHub Pages to serve files as-is
    print(f"Built site into {DIST}")


if __name__ == "__main__":
    build()

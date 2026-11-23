"""
CV website — Flask app.

Run locally:     python app.py          → http://localhost:8501
Build static:    python build.py        → dist/ (what GitHub Pages serves)
Edit content:    cv_data.py
"""

import os
import re
from datetime import date

from flask import Flask, abort, render_template
from markupsafe import Markup, escape

import cv_data

# Local preview of an unpublished dashboard change: DASHBOARD_URL=http://localhost:8503 python app.py
DASHBOARD_URL = os.environ.get("DASHBOARD_URL", cv_data.CREDIT_RISK["dashboard_url"]).rstrip("/")

app = Flask(__name__)


@app.template_filter("md")
def inline_markdown(text: str) -> Markup:
    """Escape text, then turn **bold** into <strong> and *italic* into <em>."""
    html = str(escape(text))
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)
    return Markup(html)


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=cv_data.PROFILE,
        show_phone=cv_data.SHOW_PHONE,
        hero=cv_data.HERO,
        about=cv_data.ABOUT,
        ticker=cv_data.TICKER,
        impact=cv_data.IMPACT,
        skills=cv_data.SKILLS,
        experience=cv_data.EXPERIENCE,
        education=cv_data.EDUCATION,
        affiliations=cv_data.AFFILIATIONS,
        research=cv_data.RESEARCH,
        projects=cv_data.PROJECTS,
        year=date.today().year,
    )


def credit_risk_routes() -> list[str]:
    """Every Credit Risk project page, as site paths (build.py writes each to <path>index.html)."""
    return [f"/projects/credit-risk/{p['slug'] + '/' if p['slug'] else ''}" for p in cv_data.CREDIT_RISK["pages"]]


@app.route("/projects/credit-risk/")
@app.route("/projects/credit-risk/<slug>/")
def credit_risk(slug: str = ""):
    project = cv_data.CREDIT_RISK
    page = next((p for p in project["pages"] if p["slug"] == slug), None)
    if page is None:
        abort(404)
    # Relative links keep the site working on any domain or sub-path, like the home page does.
    root = "../../" if not slug else "../../../"
    embed = f"{DASHBOARD_URL}/{page['path']}?embed=true&site=1"
    return render_template(
        "credit_risk.html",
        profile=cv_data.PROFILE,
        project=project,
        page=page,
        embed=embed,
        full_app=f"{DASHBOARD_URL}/{page['path']}",
        root=root,
        base=root + "projects/credit-risk/",
        year=date.today().year,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8501, debug=True)

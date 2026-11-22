"""
CV website — Flask app.

Run locally:     python app.py          → http://localhost:8501
Build static:    python build.py        → dist/ (what GitHub Pages serves)
Edit content:    cv_data.py
"""

import re
from datetime import date

from flask import Flask, render_template
from markupsafe import Markup, escape

import cv_data

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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8501, debug=True)

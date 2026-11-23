# Reorapetse Molefe — CV Website

Live at **https://reorapetsemolefe.co.za** (GitHub Pages, custom domain registered at domains.co.za; renews 22 Nov 2027).

A single-page, animated personal CV website. It is written in Python (Flask + Jinja templates)
and built into a static site that GitHub Pages hosts for free.

Sections: **Intro · About · Impact · Career · Education & Research · Projects · Contact**

## Project structure

```
cv-website/
├── cv_data.py              # ALL website content — edit this to update the site
├── app.py                  # Flask app (local preview server)
├── build.py                # Builds the static site into dist/
├── templates/index.html    # Page layout
├── static/
│   ├── css/style.css       # Colours, fonts, animations (colours are at the top)
│   ├── js/main.js          # Interactions: typing effect, counters, tabs, scroll reveal
│   ├── img/portrait.jpg    # Your photo
│   └── cv/Reorapetse_Molefe_CV.pdf   # Served by the "Download CV" buttons
├── .github/workflows/deploy.yml      # Auto-deploys to GitHub Pages on every push
└── requirements.txt
```

## Run it locally

```bash
cd ~/Documents/cv-website
python3 -m venv .venv            # first time only
source .venv/bin/activate
pip install -r requirements.txt  # first time only
python app.py
```

Open http://localhost:8501. The server reloads when you save a Python file. Refresh the
browser to see changes.

## Common edits

| To change… | Edit |
|---|---|
| Intro line, rotating job titles | `cv_data.py` → `HERO` |
| About me text and quick facts | `cv_data.py` → `ABOUT` |
| Scrolling highlights strip | `cv_data.py` → `TICKER` |
| Animated impact numbers | `cv_data.py` → `IMPACT` |
| Roles, bullets, per-role stats | `cv_data.py` → `EXPERIENCE` |
| Research summary | `cv_data.py` → `RESEARCH` |
| Add a project | `cv_data.py` → append to `PROJECTS` (set `status` to `"Completed"`, add `link`) |
| Credit Risk project pages (`/projects/credit-risk/…`) | `cv_data.py` → `CREDIT_RISK`; layout in `templates/credit_risk.html`. Each tab embeds a page of the Streamlit dashboard with `?embed=true&site=1` |
| Show phone / add LinkedIn or GitHub | `cv_data.py` → `SHOW_PHONE`, `PROFILE["linkedin"]`, `PROFILE["github"]` |
| Photo | Replace `static/img/portrait.jpg` (keep the file name) |
| Downloadable CV | Replace `static/cv/Reorapetse_Molefe_CV.pdf` (keep the file name) |
| Colours / fonts | Top of `static/css/style.css` |

Wrap text in `**double asterisks**` in `cv_data.py` to make it bold on the site.

## Publish changes

```bash
git add .
git commit -m "Describe your change"
git push
```

GitHub rebuilds and redeploys the site automatically within about a minute.

## Deploy (first time)

1. Create a free GitHub account at https://github.com/signup.
2. Create a new **public**, **empty** repository (no README). The name decides your address:
   - `<your-username>.github.io` → site at `https://<your-username>.github.io`
   - any other name, e.g. `cv-website` → site at `https://<your-username>.github.io/cv-website`
3. Connect this folder to it and push:
   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
   When asked for a password, use a GitHub **personal access token** (GitHub → Settings →
   Developer settings → Personal access tokens), or install the GitHub CLI
   (`brew install gh`, then `gh auth login`), which handles sign-in for you.
4. In the repository on GitHub: **Settings → Pages → Build and deployment → Source:
   GitHub Actions**. The workflow in `.github/workflows/deploy.yml` then builds and publishes
   the site. Progress shows under the **Actions** tab.

## Custom domain (already set up)

`reorapetsemolefe.co.za` is set under Settings → Pages with **Enforce HTTPS** on. DNS records at
domains.co.za: four A records (185.199.108.153, .109.153, .110.153, .111.153), four AAAA records
(2606:50c0:8000::153 … 8003::153) and `www` CNAME → `reorapetse-molefe99.github.io`.
Don't delete these records, and renew the domain before 22 Nov 2027.

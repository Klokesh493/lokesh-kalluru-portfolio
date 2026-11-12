# lokesh-kalluru-portfolio

Senior SRE, DevOps, DevSecOps, platform engineering, and AI automation portfolio site for Lokesh Reddy.

## Local Preview

Open `index.html` in a browser, or run:

```bash
python3 -m http.server 4173
```

Then visit `http://127.0.0.1:4173`.

## Publish Options

- Project page repository: `lokesh-kalluru-portfolio`
- Netlify/Vercel static deploy from this folder

## Local verification

Run `make verify` with Make and Python 3 installed. The check validates local links, fragments, and asset paths in the portfolio HTML.

## Business problem

Recruiters and engineers need a direct route from the landing page to selected projects, source code, and verification evidence.

## Project walkthrough

```mermaid
flowchart LR
    A["Browser opens GitHub Pages"]
    B["Static HTML, styles, and images load"]
    C["Visitor chooses navigation"]
    D["Selected Work cards"]
    E["GitHub Overview and source repositories"]
    A --> B --> C
    C --> D
    C --> E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

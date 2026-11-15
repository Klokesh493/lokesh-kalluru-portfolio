# Skills and verification

## What this repository demonstrates

Accessible static navigation, GitHub Pages delivery, and HTML link and asset validation.

## Reproduce the result

Run `make verify`. It checks the linked in-page IDs and local assets used by the portfolio. Reproduce the primary fixture with `python3 verify_site.py`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The local checker covers navigation structure. The public site is delivered by GitHub Pages.

[verify_site.py](../verify_site.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)

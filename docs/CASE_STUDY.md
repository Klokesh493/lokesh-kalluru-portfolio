# Lokesh Kalluru Portfolio walkthrough

## Business problem

Give visitors an accessible route from the homepage to selected work and public source repositories.

## Reproduce the workflow

Run `python3 -m http.server 4173`, then open `http://127.0.0.1:4173/#work`.

The local `make verify` run passed.

## Verification

Local checks passed.

## Limitations

The local checker covers relative files, anchor targets, and duplicate IDs. External sites are outside the checker.

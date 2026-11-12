# Lokesh Kalluru Portfolio architecture

Give visitors an accessible route from the homepage to selected work and public source repositories.

```mermaid
flowchart LR
    N0["index.html and image assets"]
    N1["GitHub Pages build"]
    N2["Browser renders project links"]
    N0 --> N1 --> N2
```

## Operational boundaries

The local checker covers relative files, anchor targets, and duplicate IDs. External sites are outside the checker.

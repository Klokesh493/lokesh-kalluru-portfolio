# Lokesh Kalluru Portfolio architecture

Give visitors an accessible route from the homepage to selected work and public source repositories.

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

## Operational boundaries

The local checker covers relative files, anchor targets, and duplicate IDs. External sites are outside the checker.

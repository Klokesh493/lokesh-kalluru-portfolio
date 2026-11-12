from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Portfolio(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            name = attrs["id"]
            if name in self.ids:
                raise ValueError(f"Duplicate element ID: {name}")
            self.ids.add(name)
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.references.append(attrs[attr])


root = Path(__file__).resolve().parent
page = Portfolio()
page.feed((root / "index.html").read_text(encoding="utf-8"))
for reference in page.references:
    target = urlsplit(reference)
    if target.scheme or target.netloc:
        continue
    path = unquote(target.path)
    if path and not (root / path).is_file():
        raise SystemExit(f"Missing local file: {reference}")
    if path in ("", "index.html") and target.fragment:
        if unquote(target.fragment) not in page.ids:
            raise SystemExit(f"Missing local fragment: {reference}")
print("Portfolio links and assets passed")

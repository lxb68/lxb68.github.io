import json
import sys
import zipfile
from pathlib import Path

from lxml import etree


path = Path(sys.argv[1])
sys.stdout.reconfigure(encoding="utf-8")
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def node_text(node):
    return "".join(node.xpath(".//w:t/text()", namespaces=ns)).strip()


with zipfile.ZipFile(path) as archive:
    names = archive.namelist()
    root = etree.fromstring(archive.read("word/document.xml"))
    body = root.find("w:body", ns)
    blocks = []
    paragraphs = []
    tables = []

    for child in body:
        kind = etree.QName(child).localname
        if kind == "p":
            text = node_text(child)
            style = ""
            styles = child.xpath("./w:pPr/w:pStyle/@w:val", namespaces=ns)
            if styles:
                style = styles[0]
            if text:
                record = {"index": len(paragraphs), "style": style, "text": text}
                paragraphs.append(record)
                blocks.append({"type": "paragraph", **record})
        elif kind == "tbl":
            rows = []
            for row in child.xpath("./w:tr", namespaces=ns):
                rows.append([node_text(cell) for cell in row.xpath("./w:tc", namespaces=ns)])
            record = {"index": len(tables), "rows": rows}
            tables.append(record)
            blocks.append({"type": "table", **record})

    payload = {
        "blocks": blocks,
        "paragraphs": paragraphs,
        "tables": tables,
        "media": [name for name in names if name.startswith("word/media/")],
        "embeddings": [name for name in names if name.startswith("word/embeddings/")],
        "headers": [name for name in names if name.startswith("word/header")],
        "footers": [name for name in names if name.startswith("word/footer")],
    }

print(json.dumps(payload, ensure_ascii=False, indent=2))

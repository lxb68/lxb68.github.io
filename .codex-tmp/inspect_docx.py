import sys
import zipfile
from pathlib import Path

from lxml import etree


sys.stdout.reconfigure(encoding="utf-8")
path = Path(sys.argv[1])
query = sys.argv[2] if len(sys.argv) > 2 else ""
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
rel_ns = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}
draw_ns = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def text(node):
    return "".join(node.xpath(".//w:t/text()", namespaces=ns)).strip()


with zipfile.ZipFile(path) as archive:
    root = etree.fromstring(archive.read("word/document.xml"))
    rel_root = etree.fromstring(archive.read("word/_rels/document.xml.rels"))
    rels = {
        node.get("Id"): node.get("Target")
        for node in rel_root.xpath("./r:Relationship", namespaces=rel_ns)
    }

blocks = []
for child in root.find("w:body", ns):
    kind = etree.QName(child).localname
    if kind == "p":
        value = text(child)
        styles = child.xpath("./w:pPr/w:pStyle/@w:val", namespaces=ns)
        style = styles[0] if styles else ""
        if value:
            blocks.append(("段落", style, value))
    elif kind == "tbl":
        rows = []
        for row in child.xpath("./w:tr", namespaces=ns):
            rows.append(" | ".join(text(cell) for cell in row.xpath("./w:tc", namespaces=ns)))
        blocks.append(("表格", "", "\n".join(rows)))

if query == "__images__":
    body_nodes = list(root.find("w:body", ns))
    for i, child in enumerate(body_nodes):
        ids = child.xpath(".//a:blip/@r:embed", namespaces=draw_ns)
        if ids:
            nearby = []
            for j in range(max(0, i - 2), min(len(body_nodes), i + 3)):
                value = text(body_nodes[j])
                if value:
                    nearby.append(f"{j}:{value[:100]}")
            print(f"XML块 {i}: " + ", ".join(f"{rid} -> {rels.get(rid)}" for rid in ids))
            print("上下文: " + " / ".join(nearby))
    raise SystemExit
elif query:
    indexes = [i for i, block in enumerate(blocks) if query in block[2]]
    selected = sorted({j for i in indexes for j in range(max(0, i - 2), min(len(blocks), i + 3))})
else:
    selected = [i for i, block in enumerate(blocks) if block[0] == "段落" and block[1] in {"1", "2", "3"}]

for i in selected:
    kind, style, value = blocks[i]
    print(f"[{i}] {kind} style={style}\n{value}\n")

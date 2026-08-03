import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from lxml import etree
from PIL import Image


sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).resolve().parents[1]
pages = [
    root / "_projects" / "dynamic-system-simulation.md",
    root / "_projects_en" / "dynamic-system-simulation.md",
]
required = {"title", "order", "track", "featured", "period", "role", "status", "cover", "tech", "summary"}


class ImageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))


errors = []
referenced = set()
for page in pages:
    raw = page.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    if len(parts) != 3:
        errors.append(f"{page.name}: Front Matter 边界缺失")
        continue
    front, body = parts[1], parts[2]
    keys = set(re.findall(r"^([a-z_]+):", front, flags=re.MULTILINE))
    missing = required - keys
    if missing:
        errors.append(f"{page.name}: 缺少字段 {sorted(missing)}")
    if 'status: "complete"' not in front:
        errors.append(f"{page.name}: 状态不是 complete")
    if re.search(r"待补充|placeholder|Details in progress", raw, flags=re.IGNORECASE):
        errors.append(f"{page.name}: 仍含占位文本")

    audit = ImageAudit()
    audit.feed(body)
    if len(audit.images) != 4:
        errors.append(f"{page.name}: 预期 4 个正文图片标签，实际 {len(audit.images)}")
    for image in audit.images:
        src = image.get("src", "")
        alt = image.get("alt", "").strip()
        if not alt:
            errors.append(f"{page.name}: 图片缺少 alt 文本")
        local = root / src.lstrip("/")
        referenced.add(local.resolve())
        if not local.is_file():
            errors.append(f"{page.name}: 图片不存在 {src}")

asset_dir = root / "images" / "project" / "dynamic-system-simulation"
for asset in asset_dir.iterdir():
    if asset.suffix.lower() == ".svg":
        etree.parse(str(asset))
    else:
        with Image.open(asset) as image:
            image.verify()
    if asset.name != "cover.svg" and asset.resolve() not in referenced:
        errors.append(f"未引用资源: {asset.name}")

if errors:
    print("验证失败：")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("验证通过：Front Matter、状态、占位文本、HTML 图片标签、资源引用、SVG/XML 与位图完整性均正常。")

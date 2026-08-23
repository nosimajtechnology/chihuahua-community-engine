#!/usr/bin/env python3
"""Build the installable Skill zip from skill/chihuahua-community-engine/.

    python scripts/build_release.py            # writes dist/chihuahua-community-engine.zip
    python scripts/build_release.py --check    # validate only, build nothing

The zip is what people upload to ChatGPT (Skills -> Create -> Upload from
your computer). ChatGPT accepts a zip whose only top-level entry is the
skill folder, so that is exactly what this produces. The folder on disk is
the source of truth; never edit a zip by hand.

Validation mirrors the upload limits published for Skills: one SKILL.md with
name and description in its front matter, every file under 25 MB, fewer than
500 files, every relative link in a markdown file resolving to a real file.
The build is deterministic - same input bytes, same zip bytes - so a rebuilt
release can be compared against a published one.
"""
import hashlib
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skill" / "chihuahua-community-engine"
DIST = ROOT / "dist"
ZIP_NAME = "chihuahua-community-engine.zip"

MAX_FILES = 500
MAX_FILE_BYTES = 25 * 1024 * 1024
# Fixed timestamp so the zip is byte-for-byte reproducible.
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")


def fail(msg):
    print(f"FAIL {msg}")
    sys.exit(1)


def validate():
    if not SKILL_DIR.is_dir():
        fail(f"missing {SKILL_DIR.relative_to(ROOT)}")
    files = sorted(p for p in SKILL_DIR.rglob("*") if p.is_file())
    if not files:
        fail("skill folder is empty")
    if len(files) > MAX_FILES:
        fail(f"{len(files)} files; the upload limit is {MAX_FILES}")

    manifests = [p for p in files if p.name.lower() == "skill.md"]
    if len(manifests) != 1:
        fail(f"expected exactly one SKILL.md, found {len(manifests)}")
    manifest = manifests[0]
    if manifest.parent != SKILL_DIR:
        fail("SKILL.md must sit at the top of the skill folder")

    text = manifest.read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not front:
        fail("SKILL.md has no front matter block")
    fields = dict(
        line.split(":", 1) for line in front.group(1).splitlines() if ":" in line
    )
    for key in ("name", "description"):
        if not fields.get(key, "").strip():
            fail(f"SKILL.md front matter is missing '{key}'")

    for p in files:
        size = p.stat().st_size
        if size > MAX_FILE_BYTES:
            fail(f"{p.relative_to(ROOT)} is {size} bytes; the limit is {MAX_FILE_BYTES}")

    for p in files:
        if p.suffix.lower() != ".md":
            continue
        for target in LINK.findall(p.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", target):
                continue  # http(s), mailto
            if not (p.parent / target).exists():
                fail(f"{p.relative_to(ROOT)} links to missing file '{target}'")

    print(f"OK   {len(files)} files, SKILL.md name={fields['name'].strip()}")
    return files


def build(files):
    DIST.mkdir(exist_ok=True)
    out = DIST / ZIP_NAME
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            arcname = f"{SKILL_DIR.name}/{p.relative_to(SKILL_DIR).as_posix()}"
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())

    with zipfile.ZipFile(out) as z:
        tops = {n.split("/", 1)[0] for n in z.namelist()}
        if tops != {SKILL_DIR.name}:
            fail(f"zip must contain exactly one top-level folder, got {sorted(tops)}")

    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    (DIST / "SHA256SUMS").write_text(f"{digest}  {ZIP_NAME}\n", encoding="utf-8")
    print(f"OK   {out.relative_to(ROOT)} ({out.stat().st_size} bytes)")
    print(f"OK   sha256 {digest}")


if __name__ == "__main__":
    found = validate()
    if "--check" not in sys.argv:
        build(found)

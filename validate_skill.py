#!/usr/bin/env python3
"""Small offline structural checks for the OpenCut AI skill package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
errors = []
text = SKILL.read_text(encoding="utf-8") if SKILL.exists() else ""
if not text.startswith("---\n"):
    errors.append("SKILL.md must start with YAML frontmatter")
else:
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append("SKILL.md frontmatter closing delimiter is missing")
    else:
        front = parts[1]
        name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", front)
        desc = re.search(r"(?m)^description:\s*\"?(.+?)\"?\s*$", front)
        if not name:
            errors.append("frontmatter requires a valid lowercase name")
        elif name.group(1) != ROOT.name:
            errors.append(f"skill name '{name.group(1)}' must match folder '{ROOT.name}'")
        if not desc:
            errors.append("frontmatter requires description")
        elif len(desc.group(1)) > 1024:
            errors.append("description exceeds 1024 characters")
if len(text.splitlines()) > 500:
    errors.append("SKILL.md exceeds the recommended 500-line limit")
for required in ["README.md", "LICENSE", "references/ANDROID.md", "references/TOOLS.md", "references/ROADMAP.md", "scripts/probe_environment.py", "scripts/render_short.py"]:
    if not (ROOT / required).is_file():
        errors.append(f"missing required project file: {required}")
if errors:
    print("FAIL")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("PASS: basic OpenCut AI structure and frontmatter checks")

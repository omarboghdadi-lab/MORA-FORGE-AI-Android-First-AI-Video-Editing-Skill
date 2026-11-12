#!/usr/bin/env python3
"""Report available media tools without installing or modifying anything."""
from __future__ import annotations
import json
import platform
import shutil
import subprocess
import sys

TOOLS = ["ffmpeg", "ffprobe", "python", "python3", "node", "npm", "java", "adb", "termux-info", "whisper", "auto-editor"]

def version_for(command: str) -> str | None:
    candidates = {
        "ffmpeg": ["-version"], "ffprobe": ["-version"],
        "python": ["--version"], "python3": ["--version"],
        "node": ["--version"], "npm": ["--version"], "java": ["-version"],
        "adb": ["version"], "termux-info": [], "whisper": ["--help"],
        "auto-editor": ["--version"],
    }
    try:
        p = subprocess.run([command, *candidates[command]], capture_output=True, text=True, timeout=4)
        output = (p.stdout or p.stderr).strip().splitlines()
        return output[0][:240] if output else f"available (exit {p.returncode})"
    except Exception as exc:  # diagnostics must never crash on an absent/broken tool
        return f"detected but could not query: {type(exc).__name__}"

def main() -> int:
    found = {}
    for tool in TOOLS:
        path = shutil.which(tool)
        found[tool] = {"path": path, "version": version_for(tool) if path else None}
    report = {
        "project": "OpenCut AI",
        "diagnostic_only": True,
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "tools": found,
        "notes": [
            "No software was installed or changed.",
            "Detection does not prove that a tool can process every media format.",
            "Android native Media3 APIs are available only inside a compatible Android app, not as a shell command.",
        ],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

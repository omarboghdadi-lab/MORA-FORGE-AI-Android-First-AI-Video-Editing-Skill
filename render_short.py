#!/usr/bin/env python3
"""Render a simple vertical short with FFmpeg; preserves source files."""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def probe(path: Path) -> dict:
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        raise RuntimeError("ffprobe is required to verify the rendered output")
    p = run([ffprobe, "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height", "-of", "json", str(path)])
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or "ffprobe failed")
    return json.loads(p.stdout)


def render(source: Path, destination: Path, width: int = 1080, height: int = 1920,
           start: float | None = None, duration: float | None = None) -> dict:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg was not found on PATH")
    if source.resolve() == destination.resolve():
        raise ValueError("Output must not overwrite the input file")
    if width <= 0 or height <= 0 or width % 2 or height % 2:
        raise ValueError("Width and height must be positive even numbers")
    if not source.is_file():
        raise FileNotFoundError(f"Input file does not exist: {source}")
    if start is not None and start < 0:
        raise ValueError("Start time cannot be negative")
    if duration is not None and duration <= 0:
        raise ValueError("Duration must be greater than zero")
    destination.parent.mkdir(parents=True, exist_ok=True)
    vf = f"scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height},setsar=1"
    cmd = [ffmpeg, "-hide_banner", "-y"]
    if start is not None:
        cmd += ["-ss", str(start)]
    cmd += ["-i", str(source)]
    if duration is not None:
        cmd += ["-t", str(duration)]
    cmd += ["-map", "0:v:0", "-map", "0:a?", "-vf", vf,
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
            "-movflags", "+faststart", str(destination)]
    p = run(cmd)
    if p.returncode:
        raise RuntimeError(p.stderr[-3000:] or "FFmpeg render failed")
    if not destination.is_file() or destination.stat().st_size == 0:
        raise RuntimeError("FFmpeg returned success but no output file was created")
    metadata = probe(destination)
    streams = metadata.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    if not video or video.get("width") != width or video.get("height") != height:
        raise RuntimeError("Output verification failed: video stream or expected dimensions missing")
    return {"output": str(destination), "bytes": destination.stat().st_size,
            "duration": metadata.get("format", {}).get("duration"), "streams": streams}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    parser.add_argument("--start", type=float)
    parser.add_argument("--duration", type=float)
    args = parser.parse_args()
    try:
        print(json.dumps(render(args.input, args.output, args.width, args.height, args.start, args.duration), indent=2))
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())

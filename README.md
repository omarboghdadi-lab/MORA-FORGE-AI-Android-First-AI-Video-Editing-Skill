# OpenCut AI

**Android-First AI Video Editing Skill for Shorts, Reels, and TikTok**

OpenCut AI is an open-source Agent Skill that helps compatible AI coding agents plan, automate, and verify short-form video edits. It is designed Android-first, with Windows and Linux support planned through capability detection.

> **Status: early scaffold (v0.1.0).** This repository is not yet a complete video editor or Android application. The first release provides workflow instructions, a tool-selection strategy, environment diagnostics, and validation tests. Editing operations become executable only when a compatible engine is installed and available to the agent.

## What it aims to cover

- Timeline planning, trimming, concatenation, reframing, and export
- Captions, transcription, and subtitle timing
- Narration, music, sound effects, cleanup, and mixing
- Color correction, overlays, transitions, motion graphics, and visual effects
- Social-video presets, quality checks, and reproducible project manifests

## Install as an Agent Skill

Copy the `opencut-ai/` folder into the skills directory supported by your agent client. Skill discovery paths differ by product; consult that client's current documentation. The portable format is based on the open Agent Skills specification.

## Android reality check

A Skill is instructions plus optional scripts; it is not itself an Android app, codec, or media engine. On Android, the most reliable full application path is a native app using AndroidX Media3 Transformer. A shell-based path may use a compatible FFmpeg build (for example in Termux), but support varies by device, Android version, package source, and storage permissions. See [`references/ANDROID.md`](references/ANDROID.md).

## Tool philosophy

No single tool covers every editing task. OpenCut AI uses capability detection and optional integrations rather than treating every dependency as mandatory. See [`references/TOOLS.md`](references/TOOLS.md).

## Quick diagnostic

```bash
python scripts/probe_environment.py

# Render a vertical short (requires ffmpeg + ffprobe)
python scripts/render_short.py input.mp4 output.mp4 --start 0 --duration 30
```

This reports tools detected on the current machine. It does not install anything or process media.

## Development checks

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
```

## Roadmap

See [`references/ROADMAP.md`](references/ROADMAP.md). The first implementation milestone is a verified FFmpeg-based command-line workflow on desktop and a separately validated Android execution path. A native Android Media3 adapter is a later milestone.

## Licensing

The OpenCut AI scaffold is licensed under MIT. Third-party tools, codecs, models, fonts, music, and assets retain their own licenses. Do not assume that bundling or redistributing them is permitted. In particular, FFmpeg's build configuration affects its LGPL/GPL obligations; see the official [FFmpeg legal page](https://ffmpeg.org/legal.html).

## Contributing

Issues and pull requests are welcome. Please include OS/device details, tool versions, a minimal reproduction, and test results. Never upload private footage or credentials in bug reports.

# MORA-FORGE-AI

**Android-first AI video editing skill for Shorts, Reels, and TikTok.**

MORA-FORGE-AI is an extensible editing workflow designed to help an AI coding agent inspect media, plan an edit, use available media tools, review the result, and export finished videos.

## Project status

**Foundation stage — not yet a complete video editor.**

This repository currently provides the skill instructions and architecture documents. Actual editing depends on media-processing tools being installed and tested in the execution environment.

## First target

- Accept user-provided video, audio, and image assets.
- Inspect source media and identify duration, dimensions, frame rate, and audio streams.
- Create an edit plan before processing.
- Use FFmpeg when it is installed and suitable.
- Produce vertical 9:16 social-video exports by default when requested.
- Review the output and report any limitations honestly.
- Preserve original files; write outputs to a separate directory.

## Skill location

The Codex-discoverable skill is located at:

`.agents/skills/mora-forge-ai/SKILL.md`

## Design principles

1. Android-first workflow; do not assume desktop tools run natively on Android.
2. Cloud execution is allowed when the connected environment supports it.
3. Platform-independent instructions; avoid hard-coding one AI assistant.
4. Verify tool availability before using it.
5. Never claim an export succeeded unless the output file exists and has been checked.
6. Protect user media and do not upload it to third-party services without permission.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Roadmap](docs/ROADMAP.md)
- [Tool compatibility](docs/TOOL-COMPATIBILITY.md)

## License

All rights reserved. No permission is granted to copy, modify, distribute, or commercially use this project except as expressly authorized in writing by the copyright holder. Third-party tools and dependencies remain subject to their own licenses.

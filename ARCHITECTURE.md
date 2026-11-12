# Architecture

MORA-FORGE-AI separates editing decisions from media execution.

## Core stages

1. **Brief interpreter** — extracts platform, duration, style, language, and delivery requirements.
2. **Media inspector** — inventories inputs and reads technical metadata.
3. **Edit planner** — produces a timeline and an execution plan.
4. **Capability registry** — records which tools are installed and verified in the current environment.
5. **Execution orchestrator** — runs the selected processing steps without modifying originals.
6. **Quality reviewer** — checks the rendered output and reports limitations.
7. **Export manager** — writes final deliverables and metadata.

## Execution model

The skill instructions can be used by different AI assistants. The actual processing engine is environment-specific. A cloud workspace may run command-line tools such as FFmpeg if they are installed and configured.

## Important boundary

The skill is not itself a video codec, editor, mobile application, or cloud service. Those capabilities must be supplied by the host environment and verified at runtime.

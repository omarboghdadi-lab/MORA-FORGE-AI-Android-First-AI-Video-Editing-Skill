# Tool matrix (planned, capability-gated)

| Tool | Intended use | Android status | Windows/Linux status | Required? |
|---|---|---|---|---|
| AndroidX Media3 Transformer | Native Android editing/export | Preferred in a native Android app | Not applicable | Android app milestone |
| FFmpeg / ffprobe | Trim, mux, transcode, filters, audio, export, inspection | Optional; verify build/runtime | Preferred baseline | Optional but recommended |
| Whisper | Speech recognition and timestamps | Model/runtime dependent; heavy | Supported when installed | Optional |
| DeepFilterNet | Speech denoising | Runtime/model dependent | Supported when installed | Optional |
| OpenCV | Frame analysis, image processing | Native integration required | Supported when installed | Optional |
| Remotion | Programmatic motion graphics | Not a native Android engine | Node/browser environment | Optional |
| MoviePy | Python editing orchestration | Python runtime and dependencies required | Python environment | Optional |
| Auto-Editor | Silence/scene-based rough cuts | Verify Python/FFmpeg compatibility | Verify installation | Optional |
| Audio Separator | Stem/source separation | Model/runtime dependent; often resource intensive | Supported when installed | Optional |

## Selection rules

- Detect first; do not install silently.
- Prefer platform-native acceleration on Android for common export operations.
- Prefer FFmpeg for deterministic CLI processing when a compatible build exists.
- Use Whisper, DeepFilterNet, OpenCV, Remotion, MoviePy, Auto-Editor, and Audio Separator only when their dependencies are available and the task benefits from them.
- Record exact versions and commands in the project report.
- Check each dependency's license and model-weight terms before bundling or redistributing.

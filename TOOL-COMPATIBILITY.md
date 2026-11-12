# Tool compatibility

This document is a list of candidates, not a claim that these tools are installed or supported.

| Tool | Potential role | Verification required |
|---|---|---|
| FFmpeg | Media inspection, trimming, encoding, audio mixing | Check executable, codecs, filters, and build configuration |
| Whisper | Speech transcription | Check runtime, model availability, and compute requirements |
| DeepFilterNet | Speech denoising | Check installation, model files, and audio format support |
| OpenCV | Frame/image analysis | Check package and codec support |
| MoviePy | Python-based editing workflows | Check Python version and dependencies |
| Remotion | Programmatic motion graphics | Check Node.js and browser/render dependencies |
| Auto-Editor | Silence and content-aware editing | Check installation and supported media formats |
| Audio Separator | Stem separation | Check model/runtime and hardware requirements |
| Android Media3 Transformer | Native Android media processing | Requires an Android application integration |
| AVFoundation | Native Apple-platform media processing | Requires an iOS/macOS application integration |

## Compatibility policy

- Detect tools at runtime.
- Record versions and relevant capabilities.
- Test a small sample before processing a full project.
- Never infer mobile support from desktop support.
- Keep optional AI models separate from the basic FFmpeg workflow.

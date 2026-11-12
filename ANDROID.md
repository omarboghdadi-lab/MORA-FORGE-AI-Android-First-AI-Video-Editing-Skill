# Android support strategy

## Important distinction

The Agent Skill format does not grant Android filesystem, media codec, GPU, or app permissions. The host agent must expose a shell or other execution tool, and the user must grant access to the chosen media files.

## Preferred native route: AndroidX Media3 Transformer

For a real Android application, use AndroidX Media3 Transformer for supported editing and export operations. It supports trimming, transcoding, track removal, scaling/rotation, custom effects, and image-to-video workflows. It uses Android media components and OpenGL effects. Check the current official Android documentation and the selected Media3 version before implementation.

## Optional shell route: Termux + FFmpeg

- Treat Termux and FFmpeg as optional capabilities, not guaranteed dependencies.
- Installation source and package availability matter; use the current official Termux guidance.
- Check `command -v ffmpeg` and `ffmpeg -version` before attempting a render.
- Check `ffprobe` separately; some packages/builds may not provide it.
- Android scoped storage and shared-storage permissions can prevent access to media paths. Ask the user to select/copy files into an accessible project directory rather than bypassing permissions.
- Long renders may be interrupted by battery optimization, thermal throttling, low memory, or process lifecycle limits.
- Never promise desktop parity or 4K performance without device-specific tests.

## Android milestones

1. Validate a minimal FFmpeg smoke test on a real device and record device/Android/Termux/package versions.
2. Test read/write access using a user-selected sample clip.
3. Benchmark trim, scale, overlay, audio mix, subtitles, and H.264/AAC export independently.
4. Implement a native Media3 adapter for operations where shell FFmpeg is unavailable or inefficient.
5. Add resumable jobs, progress reporting, cancellation, free-space checks, and thermal/resource safeguards.

## Official references

- https://developer.android.com/media/media3/transformer
- https://developer.android.com/media/media3/transformer/getting-started
- https://termux.dev/en/

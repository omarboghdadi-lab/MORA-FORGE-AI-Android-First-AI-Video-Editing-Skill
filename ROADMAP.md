# Roadmap

## Phase 0 — Foundation (current scaffold)
- [x] Define the portable Agent Skill structure.
- [x] Document Android-first architecture and capability-based routing.
- [x] Add environment diagnostics and basic validation tests.
- [ ] Validate the skill with the official Agent Skills reference validator.

## Phase 1 — Desktop MVP (Windows/Linux)
- [ ] Build a safe FFmpeg wrapper with argument arrays (no shell interpolation).
- [ ] Probe media and produce JSON metadata.
- [ ] Implement trim, concat, scale/crop to 9:16, audio mix, subtitles, and H.264/AAC export.
- [ ] Add automated sample-media integration tests.

## Phase 2 — Android MVP
- [ ] Validate Termux/FFmpeg on multiple Android devices.
- [ ] Document scoped-storage workflow and performance limits.
- [ ] Build a native Android Media3 Transformer adapter or companion app.
- [ ] Add progress, cancellation, storage checks, and recovery from interrupted exports.

## Phase 3 — AI-assisted editing
- [ ] ASR/transcription and subtitle alignment.
- [ ] Scene detection and rough-cut suggestions.
- [ ] Voice cleanup and loudness-aware audio mixing.
- [ ] Optional visual analysis and content-aware reframing.

## Phase 4 — Advanced post-production
- [ ] Motion graphics templates and reusable transitions.
- [ ] Color correction and advanced compositing.
- [ ] Optional stem separation and advanced denoising.
- [ ] Platform-specific export validation profiles.

## Release gates

A feature is not marked complete until it has: a documented capability check, a working implementation, a test or reproducible manual test, clear failure handling, and license review for bundled dependencies.

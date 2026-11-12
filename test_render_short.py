import importlib.util
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "render_short.py"
spec = importlib.util.spec_from_file_location("render_short", SCRIPT)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)

class RenderTests(unittest.TestCase):
    def test_rejects_same_input_and_output(self):
        with self.assertRaises(ValueError):
            renderer.render(Path("same.mp4"), Path("same.mp4"))

    def test_rejects_odd_dimensions(self):
        with self.assertRaises(ValueError):
            renderer.render(Path("input.mp4"), Path("out.mp4"), width=101, height=201)

    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "FFmpeg/ffprobe not installed")
    def test_renders_and_verifies_tiny_sample(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "sample.mp4"
            dst = Path(tmp) / "short.mp4"
            cmd = [shutil.which("ffmpeg"), "-v", "error", "-f", "lavfi", "-i", "testsrc=size=320x240:rate=24:duration=1", "-f", "lavfi", "-i", "sine=frequency=440:duration=1", "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(src)]
            made = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(made.returncode, 0, made.stderr)
            result = renderer.render(src, dst, width=180, height=320)
            self.assertTrue(dst.exists())
            self.assertGreater(result["bytes"], 0)
            video = next(s for s in result["streams"] if s["codec_type"] == "video")
            self.assertEqual((video["width"], video["height"]), (180, 320))
            self.assertTrue(any(s["codec_type"] == "audio" for s in result["streams"]))

if __name__ == "__main__":
    unittest.main()

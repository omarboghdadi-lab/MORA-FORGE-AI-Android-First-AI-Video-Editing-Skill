import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "probe_environment.py"
spec = importlib.util.spec_from_file_location("probe_environment", SCRIPT)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

class ProbeTests(unittest.TestCase):
    def test_version_for_missing_command_is_safe(self):
        self.assertIsInstance(probe.version_for("definitely-not-a-real-opencut-command"), str)

    def test_tool_list_contains_core_media_tools(self):
        self.assertIn("ffmpeg", probe.TOOLS)
        self.assertIn("ffprobe", probe.TOOLS)

if __name__ == "__main__":
    unittest.main()

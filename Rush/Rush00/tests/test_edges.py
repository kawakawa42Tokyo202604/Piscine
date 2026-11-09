"""Exercise all five rectangle patterns with degenerate dimensions."""

from __future__ import annotations

import os
from pathlib import Path
import shlex
import subprocess
import tempfile
from typing import ClassVar
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [("o-o", "| |", "o-o"), ("/*\\", "* *", "\\*/"),
            ("ABA", "B B", "CBC"), ("ABC", "B B", "ABC"),
            ("ABC", "B B", "CBA")]


def rectangle(pattern: tuple[str, str, str], width: int, height: int) -> str:
    if width <= 0 or height <= 0:
        return ""
    rows = []
    for row in range(height):
        border = pattern[0] if row == 0 else (
            pattern[2] if row == height - 1 else pattern[1])
        line = border[0] if width == 1 else (
            border[0] + border[1] * (width - 2) + border[2])
        rows.append(line + "\n")
    return "".join(rows)


class Rush00Tests(unittest.TestCase):
    workspace: ClassVar[tempfile.TemporaryDirectory[str]]
    programs: ClassVar[list[Path]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace = tempfile.TemporaryDirectory(prefix="rush00-test-")
        cls.addClassCleanup(cls.workspace.cleanup)
        cls.programs = []
        for pattern in range(5):
            binary = Path(cls.workspace.name) / f"rush{pattern:02d}"
            command = shlex.split(os.environ.get("CC", "cc"))
            command += shlex.split(os.environ.get(
                "TEST_CFLAGS", "-Wall -Wextra -Werror"))
            command += [str(ROOT / "tests/driver.c"),
                        str(ROOT / "ft_putchar.c"),
                        str(ROOT / f"rush{pattern:02d}.c"), "-o", str(binary)]
            subprocess.run(command, check=True)
            cls.programs.append(binary)

    def test_patterns_and_edge_dimensions(self) -> None:
        sizes = [(1, 1), (1, 4), (5, 1), (2, 2), (5, 3), (20, 4),
                 (0, 3), (3, 0), (-1, 3), (3, -1), (-2147483648, 1)]
        for index, binary in enumerate(self.programs):
            for width, height in sizes:
                with self.subTest(pattern=index, width=width, height=height):
                    result = subprocess.run(
                        [str(binary), str(width), str(height)],
                        capture_output=True, text=True, timeout=3,
                        cwd=self.workspace.name)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stdout,
                                     rectangle(PATTERNS[index], width, height))


if __name__ == "__main__":
    unittest.main()

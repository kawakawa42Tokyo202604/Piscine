"""Map validation and a brute-force oracle for small BSQ inputs."""

from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def solved(rows: list[str], empty: str = ".", fill: str = "x") -> str:
    best = (0, 0, 0)
    for row in range(len(rows)):
        for col in range(len(rows[0])):
            limit = min(len(rows) - row, len(rows[0]) - col)
            for size in range(1, limit + 1):
                if size <= best[0]:
                    continue
                if all(rows[y][x] == empty
                       for y in range(row, row + size)
                       for x in range(col, col + size)):
                    best = (size, row, col)
    result = [list(line) for line in rows]
    size, row, col = best
    for y in range(row, row + size):
        for x in range(col, col + size):
            result[y][x] = fill
    return "".join("".join(line) + "\n" for line in result)


class BSQTests(unittest.TestCase):
    def setUp(self) -> None:
        workspace = tempfile.TemporaryDirectory(prefix="bsq-test-")
        self.addCleanup(workspace.cleanup)
        self.work = Path(workspace.name)

    def call(self, args: list[str], data: str = ""
             ) -> subprocess.CompletedProcess[str]:
        return subprocess.run([str(ROOT / "bsq"), *args], input=data,
                              text=True, capture_output=True,
                              cwd=self.work, timeout=5)

    def test_small_maps_from_files_and_stdin(self) -> None:
        cases = [["."], ["o"], ["....."], [".", ".", "."],
                 [".....", ".....", "....."], ["ooo", "ooo"],
                 ["..o..", "..o..", "ooooo"],
                 ["....", ".o..", "....", "...."]]
        for rows in cases:
            text = f"{len(rows)}.ox\n" + "\n".join(rows) + "\n"
            (self.work / "map.txt").write_text(text)
            for args, data in [(["map.txt"], ""), ([], text)]:
                with self.subTest(rows=rows, stdin=not args):
                    result = self.call(args, data)
                    self.assertGreaterEqual(result.returncode, 0)
                    self.assertEqual(result.stderr, "")
                    self.assertEqual(result.stdout, solved(rows))

    def test_custom_symbols_and_multiple_files(self) -> None:
        (self.work / "a").write_text("2_#@\n___\n___\n")
        (self.work / "b").write_text("1.ox\n.\n")
        result = self.call(["a", "b"])
        self.assertEqual(result.stdout, "@@_\n@@_\n\nx\n")
        self.assertEqual(result.stderr, "")

    def test_invalid_maps_are_rejected_without_crashing(self) -> None:
        cases = ["", "1.ox\n", "1.ox\n\n", "2.ox\n.\n", "0.ox\n.\n",
                 "1.o\n.\n", "1..x\n.\n", "1.ox\nz\n",
                 "2.ox\n...\n..\n", "2.ox\n...\n\n...\n"]
        for text in cases:
            with self.subTest(text=text):
                (self.work / "invalid").write_text(text)
                result = self.call(["invalid"])
                self.assertGreaterEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertEqual(result.stderr, "map error\n")
        result = self.call(["does-not-exist"])
        self.assertGreaterEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "map error\n")


if __name__ == "__main__":
    unittest.main()

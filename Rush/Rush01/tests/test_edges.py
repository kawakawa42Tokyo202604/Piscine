"""Validate solver output independently of its chosen solution."""

from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def visible(values: list[int]) -> int:
    maximum = 0
    count = 0
    for value in values:
        if value > maximum:
            maximum = value
            count += 1
    return count


def hints_for(board: list[list[int]]) -> list[int]:
    columns = [list(column) for column in zip(*board)]
    return ([visible(column) for column in columns]
            + [visible(column[::-1]) for column in columns]
            + [visible(row) for row in board]
            + [visible(row[::-1]) for row in board])


class Rush01Tests(unittest.TestCase):
    def setUp(self) -> None:
        workspace = tempfile.TemporaryDirectory(prefix="rush01-test-")
        self.addCleanup(workspace.cleanup)
        self.work = workspace.name

    def call(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        return subprocess.run([str(ROOT / "rush-01"), *args],
                              capture_output=True, text=True,
                              cwd=self.work, timeout=5)

    def test_solvable_puzzles(self) -> None:
        for offset in (0, 1, 3):
            original = [[(row + col + offset) % 4 + 1 for col in range(4)]
                        for row in range(4)]
            hints = hints_for(original)
            with self.subTest(hints=hints):
                result = self.call([" ".join(map(str, hints))])
                self.assertEqual(result.returncode, 0)
                board = [list(map(int, row.split()))
                         for row in result.stdout.splitlines()]
                self.assertEqual(len(board), 4)
                self.assertTrue(all(len(row) == 4 for row in board))
                for line in [*board, *map(list, zip(*board))]:
                    self.assertEqual(sorted(line), [1, 2, 3, 4])
                self.assertEqual(hints_for(board), hints)

    def test_invalid_and_unsatisfiable_inputs(self) -> None:
        cases = [[], [""], ["1 2"], ["1 " * 15], ["1 " * 17],
                 ["0 " * 16], ["5 " * 16], ["a " * 16],
                 ["1 " * 16, "extra"], ["1 " * 16]]
        for args in cases:
            with self.subTest(args=args):
                result = self.call(args)
                self.assertGreaterEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "Error\n")


if __name__ == "__main__":
    unittest.main()

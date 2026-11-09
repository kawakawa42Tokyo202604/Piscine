"""Numeric boundaries, custom dictionaries, and invalid inputs."""

from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Rush02Tests(unittest.TestCase):
    def setUp(self) -> None:
        workspace = tempfile.TemporaryDirectory(prefix="rush02-test-")
        self.addCleanup(workspace.cleanup)
        self.work = Path(workspace.name)
        shutil.copyfile(ROOT / "numbers.dict", self.work / "numbers.dict")

    def call(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        return subprocess.run([str(ROOT / "rush-02"), *args],
                              capture_output=True, text=True,
                              cwd=self.work, timeout=5)

    def test_number_boundaries_and_leading_zeroes(self) -> None:
        cases = {"0": "zero", "0000": "zero", "1": "one", "19": "nineteen",
                 "20": "twenty", "21": "twenty one", "42": "forty two",
                 "100": "one hundred", "101": "one hundred one",
                 "110": "one hundred ten", "1000": "one thousand",
                 "1001": "one thousand one", "1000000": "one million",
                 "00042": "forty two"}
        for number, expected in cases.items():
            with self.subTest(number=number):
                result = self.call([number])
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout, expected + "\n")
                self.assertEqual(result.stderr, "")

    def test_custom_dictionary(self) -> None:
        text = (ROOT / "numbers.dict").read_text().replace("forty", "FORTY")
        (self.work / "custom.dict").write_text(text)
        result = self.call(["custom.dict", "42"])
        self.assertEqual(result.stdout, "FORTY two\n")
        self.assertEqual(result.stderr, "")

    def test_invalid_number_and_argument_count(self) -> None:
        for args in ([], [""], ["-1"], ["+1"], ["1.0"], ["abc"],
                     ["1 2"], ["1", "2", "3"]):
            with self.subTest(args=args):
                result = self.call(args)
                self.assertGreaterEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertEqual(result.stderr, "Error\n")

    def test_missing_and_incomplete_dictionaries(self) -> None:
        result = self.call(["missing.dict", "42"])
        self.assertGreaterEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "Error\n")
        (self.work / "empty.dict").write_text("")
        for number in ("0", "42", "1000"):
            with self.subTest(number=number):
                result = self.call(["empty.dict", number])
                self.assertGreaterEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertEqual(result.stderr, "Dict Error\n")

    def test_missing_required_key_does_not_print_partial_result(self) -> None:
        path = self.work / "partial.dict"
        path.write_text("40: forty\n")
        result = self.call([str(path), "42"])
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "Dict Error\n")
        path.write_text("\n40: forty\n\n2: two\n")
        result = self.call([str(path), "42"])
        self.assertEqual(result.stdout, "forty two\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()

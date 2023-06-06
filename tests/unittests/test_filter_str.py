import unittest

from src.c_filter import filter_str_start

starts_with_A = filter_str_start("A")


class TestCapitalizeNames(unittest.TestCase):
    def test_filter(self):
        names = ["Alice", "Bob", "Charlie", "Amy", "Alex"]
        expected = ["Alice", "Amy", "Alex"]

        result = starts_with_A(names)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

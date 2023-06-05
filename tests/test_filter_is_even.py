import unittest

from src.c_filter import filter_even


class TestCapitalizeNames(unittest.TestCase):
    def test_filter_even(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [2, 4, 6, 8, 10]
        result = filter_even(numbers)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

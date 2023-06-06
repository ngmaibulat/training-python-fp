import unittest

from src.d_reduce import get_max_in_arr


class Test(unittest.TestCase):
    def test_reduce(self):
        param = [1, 2, 3, 4, 5, 6, 7]
        expected = 7

        result = get_max_in_arr(param)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

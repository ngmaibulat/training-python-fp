import unittest

from src.e_partial import double


class Test(unittest.TestCase):
    def test_double(self):
        param = 10
        expected = 20

        result = double(param)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

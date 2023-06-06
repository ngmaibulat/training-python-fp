import unittest

from src.f_operator import mult_array


class Test(unittest.TestCase):
    def test_reduce(self):
        """
        This function tests the mult_array function.

        PARAMETERS:
        - self: an instance of the class that owns this test function.

        RETURNS:
        - None

        This function instantiates the input parameter and expected output
        values for the mult_array function and tests if the function returns
        the expected value. The test passes if the values match, and fails
        otherwise.
        """
        param = [1, 2, 3]
        expected = 6

        result = mult_array(param)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

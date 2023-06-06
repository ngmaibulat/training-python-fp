from src.f_operator import mult_array


def test_mult_array():
    """
    This function tests the mult_array function.

    This function instantiates the input parameter and expected output
    values for the mult_array function and tests if the function returns
    the expected value. The test passes if the values match, and fails
    otherwise.
    """
    param = [1, 2, 3]
    expected = 6

    result = mult_array(param)

    assert result == expected

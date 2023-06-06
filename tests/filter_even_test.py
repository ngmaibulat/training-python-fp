from src.c_filter import filter_even


def test_filter_even():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    result = filter_even(numbers)
    assert result == expected

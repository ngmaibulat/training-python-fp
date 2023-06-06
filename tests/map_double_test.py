from src.b_map import double_arr


def test_double_arr_empty_list():
    arr = []
    expected = []
    result = double_arr(arr)
    assert result == expected


def test_double_arr_positive_numbers():
    arr = [1, 2, 3, 4, 5]
    expected = [2, 4, 6, 8, 10]
    result = double_arr(arr)
    assert result == expected


def test_double_arr_negative_numbers():
    arr = [-1, -2, -3, -4, -5]
    expected = [-2, -4, -6, -8, -10]
    result = double_arr(arr)
    assert result == expected


def test_double_arr_mixed_numbers():
    arr = [-1, 0, 1, 2, 3]
    expected = [-2, 0, 2, 4, 6]
    result = double_arr(arr)
    assert result == expected

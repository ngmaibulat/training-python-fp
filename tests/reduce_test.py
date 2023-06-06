from src.d_reduce import get_max_in_arr


def test_get_max_in_arr():
    param = [1, 2, 3, 4, 5, 6, 7]
    expected = 7

    result = get_max_in_arr(param)

    assert result == expected

from src.e_partial import double


def test_double():
    param = 10
    expected = 20

    result = double(param)

    assert result == expected

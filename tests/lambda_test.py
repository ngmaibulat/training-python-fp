from src.a_lambda import double


def test_double():
    # arrange
    x = 10
    expected = 20

    # act
    result = double(x)

    # assert
    assert result == expected

import pytest
from src.basics.divide import divide


@pytest.fixture
def setup():
    return True


def test_divide(setup):
    # arrange
    x = 10
    y = 2
    expected = 5

    # act
    result = divide(x, y)

    # assert
    assert result == expected


def test_exception(setup):
    # arrange
    x = 10
    y = 0

    # act
    with pytest.raises(ZeroDivisionError):
        divide(x, y)

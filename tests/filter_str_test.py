from src.c_filter import filter_str_start

starts_with_A = filter_str_start("A")


def test_filter():
    names = ["Alice", "Bob", "Charlie", "Amy", "Alex"]
    expected = ["Alice", "Amy", "Alex"]

    result = starts_with_A(names)

    assert result == expected

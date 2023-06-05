is_even = lambda x: x % 2 == 0


def filter_even(numbers: list) -> list:
    even = filter(is_even, numbers)
    return list(even)


def filter_str_start(start: str):
    fn = lambda s: s.startswith(start)

    def actual(params: list):
        res = filter(fn, params)
        return list(res)

    return actual

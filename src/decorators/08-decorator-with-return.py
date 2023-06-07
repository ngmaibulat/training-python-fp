def func(fn):
    counter = [0]
    print("decorating")

    def inner_func(*args, **kwargs):
        print("inner func() called")
        res = fn(*args, **kwargs)
        counter[0] += 1
        # print(counter[0])
        return res

    return inner_func


@func
def fn1(x: int, y: int):
    return x + y


if __name__ == "__main__":
    print(fn1(1, 2))
    print(fn1(2, 2))
    print(fn1(3, 2))

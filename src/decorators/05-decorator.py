def func(fn):
    counter = [0]

    def inner_func():
        print("inner func() called")
        fn()
        counter[0] += 1
        print(counter[0])

    return inner_func


@func
def fn1():
    print("inside fn1")


if __name__ == "__main__":
    fn1()
    fn1()
    fn1()

def fn1():
    print("inside fn1")


def fn2(fn):
    print("calling function:")
    print(fn.__name__)
    fn()


fn2(fn1)

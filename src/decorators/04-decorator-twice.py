def twice(fn):
    def inner_func():
        fn()
        fn()

    return inner_func


@twice
def print_hello():
    print("Hello")


print_hello()

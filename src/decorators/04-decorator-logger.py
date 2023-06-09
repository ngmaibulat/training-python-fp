def log(fn):
    def inner_func():
        print("calling function: ", fn.__name__)
        fn()
        print("called function: ", fn.__name__)

    return inner_func


@log
def print_hello():
    print("Hello")


print_hello()

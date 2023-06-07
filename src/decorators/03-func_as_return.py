def func():
    counter = [0]

    def inner_func():
        counter[0] += 1
        print("inner_func")
        print(counter[0])

    return inner_func


if __name__ == "__main__":
    fn = func()
    fn()
    fn()
    fn()

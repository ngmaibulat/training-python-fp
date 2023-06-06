import time
from functools import wraps, reduce
from operator import mul


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

    return wrapper


@timeit
def mult_array(array):
    return reduce(mul, array)


if __name__ == "__main__":
    mult_array([23423423, 423423423, 2342342342])
    mult_array([23423423, 423423423, 2342342342])

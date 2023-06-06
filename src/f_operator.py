from operator import mul, add, sub, truediv, floordiv
from functools import reduce


def mult_array(array):
    return reduce(mul, array)

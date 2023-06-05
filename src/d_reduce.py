from functools import reduce

getmax = lambda x, y: x if x > y else y


def get_max_in_arr(arr: list):
    res = reduce(getmax, arr)
    return res

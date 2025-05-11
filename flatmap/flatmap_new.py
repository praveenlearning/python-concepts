import functools
import random
from typing import Iterable

from utils import benchmark


def flatten_recursive(values):
    res = []
    for value in values:
        if isinstance(value, Iterable):
            res.extend(flatten_recursive(value))
        else:
            res.append(value)
    return res


@benchmark
def flatten_iterative(values):
    res = []
    sample = values.copy()
    while sample:
        current = sample.pop(0)
        if isinstance(current, Iterable):
            sample = current + sample
        else:
            res.append(current)

    return res


def flatten_reduce(a, b):
    sample = [b]
    while sample:
        current = sample.pop(0)
        if isinstance(current, Iterable):
            sample = current + sample
        else:
            a.append(current)

    return a


if __name__ == '__main__':
    # nested_list = [1, list(range(100000)), [list(range(100000)), [2, 3, list(range(100000))]]]
    # benchmark(flatten_recursive)(nested_list)
    # benchmark(flatten_iterative)(nested_list)
    # benchmark(functools.reduce)(flatten_reduce, nested_list, [])


    t = functools.reduce(lambda a, _: [random.randint(-999, 999), a], range(10), [random.randint(-999, 999)])
    print(t)
    print(flatten_iterative(t))
    r = [1]
    for _ in range(10):
        r = [1, r]


    print([[1] for i in range(10)])


    print(r)
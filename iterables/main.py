from typing import Iterable


def my_product(*args: Iterable):
    pools = map(tuple, args)
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield prod


print(list(my_product((1, 2, 3), {4, 5, 6}, [7])))

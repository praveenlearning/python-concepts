from typing import Iterable, List


def my_product(*args: Iterable):
    pools = map(tuple, args)
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield prod


Numbers = List[int]


def print_nums(nums: Numbers) -> None:
    for n in nums:
        print(n)


print(list(my_product((1, 2, 3), {4, 5, 6}, [7])))
print_nums([1, 2, 3, "d"])

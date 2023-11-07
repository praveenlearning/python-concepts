# This is a sample Python script.
import math


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def zipped(*iterables):
    print(iterables)
    pools = [tuple(pool) for pool in iterables]
    length = len(pools[0])
    for i in range(length):
        try:
            yield tuple(pool[i] for pool in pools)
        except IndexError:
            return


def nCr(n: int, r: int) -> int:
    return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))


def binomial_expansion(x: int, y: int, n: int):
    # return (nCr(n, r) * x ** (n - r) * y ** r for r in range(n + 1))
    for r in range(n + 1):
        c = nCr(n, r) * x ** (n - r) * y ** r
        print(f'C{r} = {n}C{r} x {x}^{n - r} x {y}^{r} = {c}')
        yield c


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exp = binomial_expansion(2, 5, 2)
    next(exp)
    next(exp)
    next(exp)
    # print_hi('PyCharm')
    # print(list(zipped(range(50, 100), range(1000, 1050), range(101, 150))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

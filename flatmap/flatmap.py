import functools


def reduce_flatmap(f, seq):
    return functools.reduce(lambda a, b: a + b, map(f, seq))


def loop_flatmap(f, seq):
    ys = []
    for xs in seq:
        ys.extend(f(xs))
    return ys


def gen_flatmap(f, seq):
    return (ys for xs in seq for ys in f(xs))


if __name__ == '__main__':
    values = range(1, 11)


    def neighbour(x):
        return x - 1, x


    print(loop_flatmap(neighbour, values))
    print(reduce_flatmap(neighbour, values))
    print(list(gen_flatmap(neighbour, values)))

import functools

k = [("d", 100), ("a", 100), ("b", 200), ("c", 300)]

# k.sort(key=itemgetter(0), reverse=False)
# k.sort(key=itemgetter(1), reverse=True)
print(k)


def some(x, y):
    print(x, y)
    if y[1] == x[1]:
        print("reached")
        return -1 if y[0] > x[0] else 1
    return y[1] - x[1]


k.sort(key=functools.cmp_to_key(some))

print(k)

import itertools

counter = itertools.count(1, 5)

numbers = itertools.takewhile(lambda x: x < 100, counter)

print(numbers)

for x in numbers:
    print(x)

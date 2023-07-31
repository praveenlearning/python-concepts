# This is a sample Python script.

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(list(zipped(range(50, 100), range(1000, 1050), range(101, 150))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

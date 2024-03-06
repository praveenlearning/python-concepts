import functools


def singleton(cls):
    @functools.wraps(cls)
    def inner_func(*args, **kwargs):
        if not inner_func.instance:
            inner_func.instance = cls(*args, **kwargs)
        return inner_func.instance

    inner_func.instance = None
    return inner_func


@singleton
class TestClass:
    pass


@singleton
class TestClass2:
    pass


i1 = TestClass()
i2 = TestClass()
i3 = TestClass2()

print(id(i1))
print(id(i2))
print(id(i3))

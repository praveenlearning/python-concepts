class Person:
    increase_fraction = 1.04

    __slots__ = "__first", "__last", "__weight"

    def __init__(self, first: str, last: str, weight):
        self.__first = first
        self.__last = last
        self.__weight = weight

    def raise_weight(self):
        self.__weight = round(self.__weight * self.increase_fraction, 2)

    @classmethod
    def set_fraction(cls):
        pass

    @property
    def fullname(self):
        return f"{self.__first} {self.__last}"

    def route(self):
        def decorator(f):
            print(f)
            self.__weight = round(self.__weight * self.increase_fraction, 2)
            return f

        return decorator

    def __str__(self):
        return f"Person('{self.fullname}', {self.__weight})"

    def decorater(self):
        def decorate(f):
            print("running", f, "from", self)
            return f

        return decorate


tony = Person("Tony", "Stark", 64)


def decorate(f):
    print("running ", f)
    return f


@decorate
def some_one():
    print("Hello")


@tony.decorater()
def some_two():
    print("Hello")


some_one()
some_two()

class X:
    pass


class Y:
    def __call__(self, *args, **kwargs):
        print("Hello from Y")

    def some(self):
        print("Hello")



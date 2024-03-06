import time
import second
print(__name__)

if __name__ == '__main__':
    # HOF -> functions that takes functions as arguments

    def first_decorator(f):
        def wrapper(*args, **kwargs):
            print(f"Started running {f.__name__}")
            t1 = time.perf_counter()
            f(*args, **kwargs)
            t2 = time.perf_counter()
            print(f"Completed execution in {t2 - t1}")
            print()

        return wrapper


    @first_decorator
    def do_some(name: str):
        print("Hello", name)
        squares = [i * i for i in range(1000000)]

        print(sum(squares))


    @first_decorator
    def some_other(age: int):
        print("age", age)

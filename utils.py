import time
from functools import wraps
from typing import Callable, TypeVar

E = TypeVar("E")


def benchmark(f: Callable[..., E]):
    @wraps(f)
    def run(*args, **kwargs):
        t1 = time.perf_counter()
        f_result = f(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{f.__name__} completed in {(t2 - t1) * (10 ** 6)} micro seconds")
        return f_result

    return run

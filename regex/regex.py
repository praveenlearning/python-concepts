import re
from functools import wraps

domains = '''
https://www.google.com
http://isro.in
https://youtube.com
https://www.nasa.gov
'''

domain_name_pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')

print(domain_name_pattern.sub(r'\2', domains))


def function_name(name):
    def outer_wrapper(f):
        class FuncWithName:

            def __call__(self, *args, **kwargs):
                return f(*args, **kwargs)

            def __str__(self):
                return name

        return wraps(f)(FuncWithName())

    return outer_wrapper


def ask_next(f):
    @wraps(f)
    def ask(*args, **kwargs):
        x = input(f"Do you want to run {f}: ")
        if x:
            f(*args, **kwargs)

    return ask


@function_name("hello func")
@ask_next
def hello():
    """prints 'Hello' to the console"""
    print("Hello")


print(hello)
print(hello.__doc__)
hello()

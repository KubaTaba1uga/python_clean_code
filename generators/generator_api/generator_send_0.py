"""
        next() is basically the same as .send.(None)
"""


def print_more_newlines(text: str, n: int = 2) -> None:
    print(text, end="\n" * n)


def short_generator():
    for i in range(100):
        if i % 3 == 0:
            yield i


my_gen = short_generator()

print_more_newlines(f"Generator instance {my_gen}")

try:
    print_more_newlines(f".send(1) returned value {my_gen.send(1)}")
except TypeError:
    print_more_newlines("first value send to generator has to be None")

print_more_newlines(f".send(None) returned value {my_gen.send(None)}")

print_more_newlines(f"Next() returned value {next(my_gen)}")

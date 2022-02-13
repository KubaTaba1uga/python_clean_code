"""
        To return value from generator, StopIteration exception
                has to be catched.
"""
GENERATOR_MAX = 10


def generator():
    for i in range(GENERATOR_MAX):
        yield i

    return "It is done"


# Catching exception manually
my_gen = generator()

for i in range(GENERATOR_MAX):
    print(next(my_gen))

try:
    next(my_gen)
except StopIteration as result:
    print(f"Returned value is '{result.value}'")

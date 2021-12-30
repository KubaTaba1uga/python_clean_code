"""
        Generator is iterable, which create values on demand.
                List for example, create values in advance.
"""
NUMBERS_LIMIT = 100000000

# List example
long_list = [i for i in range(NUMBERS_LIMIT)]

# Generator examples
# Generator expression
long_generator = (i for i in range(NUMBERS_LIMIT))

# Generator object
def generator_obj():
    number = 0
    while number < NUMBERS_LIMIT:
        yield number
        number += 1


print("\nList takes", long_list.__sizeof__(), "bytes")

print("\nGenerator expression takes", long_generator.__sizeof__(), "bytes")

print("\nGenerator object takes", generator_obj().__sizeof__(), "bytes")

"""
        Lets create generator object which can be iterated
                over by Python for loop.
        Generator object has to produce numbers in range
                0 till infinity.
"""

# Object which behaves like generator
class InfiniteObject:
    def __init__(self):
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current_number
        self.current_number += 1
        return value


# Object which is a generator
def infinite_generator():
    current_number = 0
    while True:
        yield current_number
        current_number += 1


infinity = InfiniteObject()
for i in range(10):
    value = next(infinity)
    print(value)

print()

infinity_0 = infinite_generator()
for i in range(10):
    value = next(infinity_0)
    print(value)

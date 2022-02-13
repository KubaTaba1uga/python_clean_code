"""
        Generator chaining is when different generators are
                cumullated into one functions.
                It should be done using 'yield from <generator>' syntax.

        'yield from <generator>' syntax can be used to capture
                returned value from the generator.
"""

NAME_0 = "first"
START_0 = 0
END_0 = 5
NAME_1 = "second"


def sequence_print(name: str, start: int, end: int):
    print(f"{name} started at {start}")
    yield from range(start, end + 1)
    print(f"{name} ended at {end}")
    return end


# Generator chaining done manually
def worse_main():
    """Chain two generators into one bigger generator"""

    first_gen = sequence_print(NAME_0, START_0, END_0)

    while True:
        try:
            yield next(first_gen)
        except StopIteration as result:
            new_start = result.value
            break

    second_gen = sequence_print(NAME_1, new_start, new_start * 2)

    while True:
        try:
            yield next(second_gen)
        except StopIteration as result:
            end = result.value
            print(f"\nLast value was {end}")
            break


def main():
    """Chain two generators into one bigger generator"""

    new_start = yield from sequence_print(NAME_0, START_0, END_0)

    end = yield from sequence_print(NAME_1, new_start, new_start * 2)

    print(f"\nLast value was {end}")


print("\nMain execution:\n")
for element in main():
    print(element)

print("\nWorse Main execution:\n")
for element in worse_main():
    print(element)

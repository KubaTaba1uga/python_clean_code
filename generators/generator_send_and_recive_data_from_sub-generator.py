NAME_0 = "first"
START_0 = 0
END_0 = 5
NAME_1 = "second"


def sequence_print(name: str, start: int, end: int):
    print(f"{name} started at {start}")

    for i in range(start, end + 1):

        received = yield i

        if received:
            print(received)

    print(f"{name} ended at {end}")
    return end


def main():
    """Chain two generators into one bigger generator"""
    first_gen = sequence_print(NAME_0, START_0, END_0)

    while True:
        try:
            i = next(first_gen)

            print(i)

            if i % 2 == 0:
                first_gen.send(f"is even")

        except StopIteration as result:
            new_start = result.value
            break

    end = yield from sequence_print(NAME_1, new_start, new_start * 2)

    print(f"\nLast value was {end}")


# Send to subroutine directly
print("\nMain execution:\n")
for element in main():
    print(element)

# Send to subroutine by generator changing
m = main()
print(next(m))
m.send("It is number")
print(next(m))
m.send("It is number")
print(next(m))
m.send("It is number")

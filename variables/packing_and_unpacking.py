def sum(*numbers):
    # * indicate that content of variable
    #    should be unpacked before passing it
    #    into further
    value = 0

    for number in numbers:
        value += number

    return value


a, b, c, d = 1, 2, 3, 4
print("Unpacked sum:", sum(a, b, c, d))

# * works on any level of abstraction
a_b_c_d = (a, b, c, d)
print("Packed sum:", sum(*a_b_c_d))

# partial unpacking
first, *rest = a_b_c_d

print(f"{first=} {rest=}")

first, *rest, last = a_b_c_d

print(f"{first=} {last=} {rest=}")

a, b, c, d, *empty = a_b_c_d

print(f"{a=} {b=} {c=} {d=} {empty=}")

step = 4
numbers = (tuple(i for i in range(x, x + step)) for x in range(0, 100, step))

# unpacking works also with generators
first_sequence, *numbers = numbers
print(f"{first_sequence=}")

# unpacking can make code more cohensive
strings_generator = (f"{a=} {b=} {c=} {d=}" for (a, b, c, d) in numbers)

print("\nGenerated numbers", end="\n" * 2)
for i, string in enumerate(strings_generator):
    print(f"{i}.", string)

"""
        .throw() will raise an exception at the line where
                generator is currently suspended. If generator
                handles this exception, except clause will be called,
                otherwise exception will propagate to the caller.
"""
from time import sleep


def even_numbers():
    number = 0
    while True:

        try:
            yield number

        except RuntimeError:
            print("I need a break!!")
            sleep(3)

        number += 2


my_gen = even_numbers()
for number in my_gen:

    print(number)

    if number >= 100000:
        my_gen.close()

    elif number == 50000:
        my_gen.throw(RuntimeError)

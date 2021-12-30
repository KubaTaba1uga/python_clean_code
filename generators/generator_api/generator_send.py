"""
        .send() lets pass data to decorator dynamically.
                To do so use assign statement with yield.

        As yield return None by default, using .send()
                changes that behaviour.

        .send() is mostly used for coroutines creation, 
                like in asyncio library.
"""
from time import sleep


def even_numbers():
    number = 0
    recived_number = None

    while True:

        recived_number = yield number

        if recived_number is not None:
            print(f"Recived {recived_number}")
            sleep(3)

        else:
            number += 2


my_gen = even_numbers()
for number in my_gen:

    print(number)

    if number >= 100000:
        my_gen.close()
    elif number % 10000 == 0:
        my_gen.send(13)

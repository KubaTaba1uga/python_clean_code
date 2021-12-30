"""
        When generator.close() is being revoked, generator
                receives GeneratorExit exception. After exit signal
                no more values is being produced by it.

        Handling GeneratorExit exception is similiar to 
                try/except/finally mechanism, only more explicit.

        Use the .close() method on generator to perform 
                finishing-up tasks.
"""


def even_numbers():
    number = 0
    while True:
        yield number
        number += 2


my_gen = even_numbers()
for number in my_gen:

    if number > 100000:
        my_gen.close()
    else:
        print(number)

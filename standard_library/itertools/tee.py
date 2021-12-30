"""
        Duplicate iterators N times, syntax:
                tee(<iterator>, N)
"""
from itertools import tee
from statistics import mean


def even_numbers(stop):
    number = 0
    while number <= stop:
        yield number
        number += 2


NUMBERS_LIMIT = 99

my_gen = even_numbers(NUMBERS_LIMIT)

_max, _min, _avg = tee(my_gen, 3)

maximum, minimum, avarage = max(_max), min(_min), mean(_avg)

print("\nMaximum:", maximum)
print("Minimum:", minimum)
print("Avarage:", avarage)

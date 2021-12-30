"""
        Creates generator from iterable
"""
from itertools import islice

NUMBERS_LIMIT = 1000000

my_list = [i for i in range(NUMBERS_LIMIT)]

my_gen = islice(my_list, None)

print("\nList takes", my_list.__sizeof__(), "bytes")

print("\nGenerator  takes", my_gen.__sizeof__(), "bytes")

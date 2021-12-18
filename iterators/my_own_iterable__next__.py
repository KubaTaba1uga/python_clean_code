"""
    Iteration protocol, checks object for:
        1. __next__ or __iter__
        2. __len__ and __getitem__

    According to 1. there are two ways of
        creating iterators in python.
       
"""

# Let's imagine a object which should generate
#  dates from desired range, example:
#    since 10-10-2021
#    till  15-12-2021

from datetime import date, timedelta


class DatesIterator:
    """ Create iterable object
         using __next__ magic method
         has one main flaw, as iter()
         is revoked new iterator 
         isn't created.

        In consequence object will be
         exhausted after one full
         iteration
    """

    def __init__(self, start_at: date,
                 stop_at: date):
        self.start_at = start_at
        self.stop_at = stop_at
        self._present_day = start_at

    def __iter__(self):
        # Iterator is revoked only once
        #  at the beginning of iteration
        print("iterator revoked")
        return self

    def __next__(self):
        if self.stop_at == self._present_day:
            raise StopIteration

        today = self._present_day

        self._present_day += timedelta(days=1)
        return today


my_days = DatesIterator(start_at=date(1992, 12, 12), stop_at=date(1993, 1, 1))

for day in my_days:
    for day in my_days:
        # Onnce this loop iterate over
        #  object using next(), it is exhausted
        #  which means every next() will
        #  met StopIteration
        print(day)

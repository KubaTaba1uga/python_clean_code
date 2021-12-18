"""
    Iteration protocol, checks object for:
        1.  __next__ and __iter__
				 or
		2. __iter__

    According to this there are two ways of
        creating iterable objects in python
       
"""
# Let's imagine a object which should generate
#  dates from desired range, example:
#    since 10-10-2021
#    till  15-12-2021

from datetime import date, timedelta


class DatesIterator:
    """ Create iterable object
         using __iter__ magic method
         has one advance, as new 
         iterator is created on each 
         iter() revoke
    """

    def __init__(self, start_at: date,
                 stop_at: date):
        self.start_at = start_at
        self.stop_at = stop_at

    def __iter__(self):
        print("iterator revoked")
        present_day = self.start_at
        while present_day < self.stop_at:
            yield present_day
            present_day += timedelta(days=1)


my_days = DatesIterator(start_at=date(1992, 12, 12), stop_at=date(1993, 1, 1))

for day in my_days:
    # Generator will be created again
    #  on any iter() revoke
    for day in my_days:
        # Once this loop revoke iter()
        #  new generator will be created
        # In consequence next() won't be
        #  revoked on the object but on
        #  generator
        print(day)

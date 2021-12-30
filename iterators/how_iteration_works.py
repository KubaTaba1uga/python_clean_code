"""
        Iterable is an object which has __iter__ method implemented
                (which knows how to produce iterator).

        Iterator is an object which has __next__ method implemented
                (which knows how to produce values on at a time).
"""


class IterationExample:
    """Iterable object which is also iterator"""

    def __init__(self):
        self.start = 0
        self.stop = 5

    def __iter__(self):
        print("__iter__ revoked")
        return self.__class__()

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        print("__next__ revoked {} time".format(self.start))
        self.start += 1


iterator = IterationExample()


"""
        Manual example of for loop protocol
"""
print("Manual example of for loop protocol")

# First iterator is being created
real_iterator = iter(iterator)

for i in range(iterator.stop):
    # On each iteration next()
    # 	is revoked
    next(iterator)

# For loop stops execution when
# 	StopIteration is raised
# 	as iterator is exausted
# 	each next() revoke will
# 	raise error also
try:
    next(iterator)
except StopIteration:
    print("Iterator is exausted")

"""
	The same behaviour shown
		using for loop protocol
"""
print("\nReal example of for loop protocol")

for element in iterator:
    pass
else:
    # Else is revoked after
    # 	for loop end as for
    # 	loop protocol is
    # 	using if in each
    # 	iteration
    try:
        next(iterator)
    except StopIteration:
        print("Iterator is exausted")

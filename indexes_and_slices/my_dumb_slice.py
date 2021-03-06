class DumbSequence:
    """
       If sliced return None objects
          in place of items
    """

    def __init__(self, value=False, *values):
        if value:
            assert True, hasattr(value, "__getitem__")
            assert True, hasattr(value, "__len__")
            self._values = value
        else:
            self._values = values

    def __getitem__(self, item):
        if isinstance(item, slice):
            slice_values = self._values.__getitem__(item)
            return self._values.__class__(None for i in slice_values)

        else:
            return self._values.__getitem__(item)

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return str([item for item in self._values])


my_range = range(1, 10, 2)
my_list = [i for i in my_range]

interval = slice(1, 10, 3)

list_sequence = DumbSequence(my_list)
print(" List values:", list_sequence._values)

tuple_sequence = DumbSequence(False, 1, 3, 5, 7, 9)

print("Tuple values:", tuple_sequence._values)

print("\n Good values:", my_list[interval])

list_slice = list_sequence[interval]
print("  List slice:", list_slice)

tuple_slice = tuple_sequence[interval]
print(" Tuple slice:", tuple_slice)

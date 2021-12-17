class List:
    """
        List, Tuple or String are examples of
          sequence objects.

        Sequence is an object which implement
         __getitem__ and __len__ methods.

        Thanks to them it can be iterated over.
    """

    def __init__(self, *values):
        # Take all arguments as iterable
        self._values = list(values)

    def __getitem__(self, item):
        # If L has k return L[k]
        try:
            return self._values.__getitem__(item)

        # Return None if item doesn't exsist
        except IndexError:
            return None

    def __len__(self):
        return len(self._values)


INDEX = 1

my_list = List(1, 2, 3, 4)

print("Index notation:", my_list[INDEX])

print("  Method usage:", my_list.__getitem__(INDEX))

ERROR_INDEX = 100

print("IndexError result:", my_list[ERROR_INDEX])

print("Are errors equal?",
      my_list[ERROR_INDEX] == my_list.__getitem__(ERROR_INDEX))

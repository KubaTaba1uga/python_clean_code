class DumbList:
    """
       If sliced return None object
          in place of item
    """

    def __init__(self, *values):
        self._values = list(values)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return [None for i in
                    range(item.start or 0,
                          item.stop or self.__len__(),
                          item.step or 1)]
        else:
            return self._values.__getitem__(item)

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return str([item for item in self._values])


my_list = DumbList(1, 2, 3, 4)

print("DumbList content:", my_list)

print("Access last item:", my_list[3])

print("Slice list by step of two elements:", my_list[::2])
print("   Slice list since second element:", my_list[1:])
print("    Slice list till second element:", my_list[:1])

"""
    Using __call__(*args, **kwargs) , class can be called
        in the same way as function.

    __call__ should be used when state of object
        would be passed between calls
"""


class Fibbonacci:
    def __init__(self, how_many_numbers: int):
        self.how_many_numbers = how_many_numbers
        self.number_0 = 0
        self.number_1 = 1
        self._fibbonaci_numbers = []

    def __call__(self):
        if len(self._fibbonaci_numbers) == self.how_many_numbers:
            return self._fibbonaci_numbers

        temp_number = self.number_0 + self.number_1

        self._fibbonaci_numbers.append(temp_number)

        self.number_0, self.number_1 = self.number_1, temp_number

        return self.__call__()


def find_fibbonacci(how_many_numbers: int):

    fibbonacci_numbers = []
    number_0 = 0
    number_1 = 1

    while len(fibbonacci_numbers) < how_many_numbers:
        temp_number = number_0 + number_1

        fibbonacci_numbers.append(temp_number)

        number_0, number_1 = number_1, temp_number

    return fibbonacci_numbers


how_many_numbers = 7

print("Function result:", find_fibbonacci(how_many_numbers))

print("   Class result:", Fibbonacci(how_many_numbers)())

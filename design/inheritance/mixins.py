"""
        Mixin is a class, which encapsulates common behaviour, 
                 with goal of making the code reusable.

        On it's own it is useless, but it provides reusable
                machanism, which goal is to extend class behaviours. 
"""

# Let's imagine system which is proceeding serial numbers
#     in syntax <xyz-abc-fgh>. The need is for class, which
#     will represent the serial number.


class UppercaseIterableMixin:
    """As new system need serial number in uppercase letters
    Creating mixin is a good choice for reusable syntax change
    """

    def __iter__(self):
        return map(str.upper, super().__iter__())


class SerialNumber:
    def __init__(self, serial_number):
        self._serial_number = serial_number

    def __iter__(self):
        yield from self._serial_number.split("-")


class SerialNumberUppercase(UppercaseIterableMixin, SerialNumber):
    pass


SERIAL_NUMBER = "abc-xyz-lkjo"

serial_number = SerialNumber(SERIAL_NUMBER)

print(list(serial_number))

serial_number_uppercase = SerialNumberUppercase(SERIAL_NUMBER)

print(list(serial_number_uppercase))

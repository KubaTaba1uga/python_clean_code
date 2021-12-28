"""
        One of common descriptor use case is creating
                validator.
"""
from abc import ABC, abstractmethod


class Validator(ABC):
    """Abstract class for Validators creating"""

    def __set_name__(self, type, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, type=None):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        """Validate value"""
        ...


class OneOf(Validator):
    """Verifies that value is one of a restricted set of options"""

    def __init__(self, *options):
        self.options = options

    def validate(self, value):
        if value not in self.options:
            raise ValueError("Value is not in setted options")


class Number(Validator):
    """Verifies that a value is either an int or float. Optionally,
    it verifies that a value is between a given minimum
    or maximum."""

    def __init__(self, minimum=None, maximum=None):
        self.minimum = minimum
        self.maximum = maximum

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("{value} has to be integer or float type")

        if self.minimum and value < self.minimum:
            raise ValueError(f"{value} has to be bigger than {self.minimum}")

        if self.maximum and value > self.maximum:
            raise ValueError(f"{value} has to be smaller than {self.maximum}")


class String(Validator):
    """Verifies that a value is a string. Optionally, it validates a
     given minimum or maximum length. It can validate
    a user-defined predicate as well."""

    def __init__(self, min_length=None, max_length=None, predicate=None):
        self.min_length = min_length
        self.max_length = max_length
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"{value} has to be a string")

        if self.min_length and len(value) < self.min_length:
            raise ValueError(
                f"{value} is smaller than required length = {self.min_length}"
            )

        if self.max_length and len(value) > self.max_length:
            raise ValueError(
                f"{value} is bigger than required length = {self.max_length}"
            )

        if self.predicate and not self.predicate(value):
            raise ValueError(f"{value} not met {self.predicate}")


class User:
    first_name = String(min_length=2, predicate=str.isupper)
    last_name = String(min_length=2, predicate=str.isupper)
    age = Number(minimum=0, maximum=99)
    user_type = OneOf("normal", "admin")

    def __init__(self, first_name, last_name, age, user_type="normal"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_type = user_type


user_example = {
    "first_name": "JAKUB",
    "last_name": "Lama",
    "age": 87,
    "user_type": "admin",
}

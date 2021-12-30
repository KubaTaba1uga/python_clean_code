"""
        __slots__ class attributes is used to ensure instances compliance.
                After defining attributes as __slots__ arguments, only them
                could be added to instance but no more.

        Classes with __slot__ attribute don't have __dict__ attribute.

        It should be used when object shouldn't have dynamic attributes
                capabalities.
"""


class StaticClass:
    __slots__ = ("name", "value")

    def __init__(self, name, value):
        self.name = name
        self.value = value


example_data = {"name": "babyBot", "value": 23}

example = StaticClass(**example_data)

# This is allowed
example.name = "adultBot"
print("Before dynamic attribute assignment", dir(example), end="\n\n")
# This is not
try:
    example.second_name = "babyBot"
except AttributeError as e:
    print(e)

print("After dynamic attribute assignment", dir(example))

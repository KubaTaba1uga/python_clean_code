"""
         Don't use mutable objects as default function arguments.
         
         Default arguments are created once, at function declaration,
               so after first function execution, the arguments will be 
               exausted.
"""


def wrong_function(user={"name": "John", "age": 23}):
    name = user.pop("name")
    age = user.pop("age")

    print(name, "is", age, "years old\n")


def good_function(user: dict = None):
    user = user or {"name": "John", "age": 23}

    name = user.pop("name")
    age = user.pop("age")

    print(name, "is", age, "years old\n")


# After first function revoke
#  default argument is no longer
#  valid
wrong_function()

try:
    wrong_function()
except KeyError:
    print("Default arguments are exausted\n")


for i in range(3):
    good_function()

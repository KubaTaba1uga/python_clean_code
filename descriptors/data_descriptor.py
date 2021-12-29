"""
        Descriptor which define __set__ or __set_name__
                method, is called data descriptor, as it is
                have access to objects data.
"""


class DataDescriptor:
    def __set_name__(self, instance_class, public_name):
        self.private_name = "_" + public_name

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)

    def __get__(self, instance, instance_class):
        return "Get is working"


class User:
    password = DataDescriptor()

    def __init__(self, password):
        self.password = password


print(f"{User.password=}")

me = User("*******************")

print(f"{me.password=}")
print(f"{me.__dict__=}")

# If __delete__ method is not defined
#       del keywoard will raise exception
del me.password

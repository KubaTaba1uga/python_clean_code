"""
        Descriptor which doesn't define __set__ and __delete__
                methods, is called non-data descriptor, as it is
                not having capability to access objects data.

        Non data descriptors are revoked only when object
                __dict__ is not populated with descriptor attribute.
"""


class NonDataDescriptor:
    def __get__(self, instance, type):
        return self


class User:
    password = NonDataDescriptor()

    def __init__(self, password):
        self.password = password


# Descriptors __get__ will be revoked because
#       User.__dict__ is empty
print(f"{User.__dict__=}")

# Descriptor __get__ won't be revoked because
#       me.__dict__ is populated with 'password' key
#       which overwrites descriptor attribute
me = User("**************")
print(f"{me.__dict__=}")
del me.password

# When me.__dict__ doesn't have 'password' key
#       descriptor __get__ will be revoked
print(f"{me.__dict__=}")
print(me.password)

class ProtectedAttribute:
    """Assign None value, in place of attribute deletion"""

    def __set_name__(self, type, public_name):
        self.private_name = "_" + public_name

    def __delete__(self, instance):
        setattr(instance, self.private_name, None)

    def __get__(self, instance, type=None):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)


class User:
    email = ProtectedAttribute()

    def __init__(self, email):
        self.email = email

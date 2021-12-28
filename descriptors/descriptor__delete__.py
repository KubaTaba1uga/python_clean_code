class ProtectedAttribute:
    """Assign None value, in place of attribute deletion"""

    def __set__name__(self, type, value_name):
        self.value_name = value_name

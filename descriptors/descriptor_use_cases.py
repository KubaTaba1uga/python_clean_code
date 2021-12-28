"""
        Descriptors defined within __set__ magic method are used in
                scenarios like:
                        1. Managed attribute - hiding private attribute
                                under descriptor interface
                        2. Customized names - inform descriptor which
                                attribute name was used
\
        The main motivation for descriptors is to provide a hook allowing
         objects stored in class variables to control what happens during
         attribute lookup and setup.
"""
import logging

logging.basicConfig(level=logging.INFO)

# Managed attribute
# When public attribute is accessed,
#       it is done using descriptor interface
# Main issue is hardwiring attribute
#       name in LoggedAgeAccess, which
#       make class not flexible enough
class BadLoggedAccess:
    """Managed attribute descriptor example"""

    def __get__(self, instance, type):
        value = instance._age
        logging.info("Accessing %r giving %r", "age", value)
        return value

    def __set__(self, instance, value):
        logging.info("Updating %r to %r", "age", value)
        instance._age = value


class BadUser:
    """Managed attribute client example"""

    age = BadLoggedAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


# Customized Names
# Using customized names descriptor
#       could be informed about attribute
#       which is currently accesed
# Private attributes are created dynamically
#       which makes descriptor more flexible
class GoodLoggedAccess:
    """Cusomized names descriptor example"""

    def __set_name__(self, type, name):
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, type):
        value = getattr(instance, self.private_name)
        logging.info("Accessing %r giving %r", "age", value)
        return value

    def __set__(self, instance, value):
        # Object instances will contain only private
        #       attributes as self.private_name is used
        #       for value setting. Try <instance>.__dir__
        setattr(instance, self.private_name, value)
        logging.info("Updating %r to %r", "age", value)


class GoodUser(BadUser):
    """Customized names client example"""

    name = GoodLoggedAccess()
    age = GoodLoggedAccess()

"""
	When attribute is accessd __getattribute__ is
		revoked first, when method can not found
		desired value, __getattr__ is called.

	Overwriting __getattribute__ should be used to
		control way object attributes are obtained.

	Overwriting __getattr_ should be used to
		control object's dynamic attributes behaviour.
"""


class DynamicAttributes:
    def __init__(self):
        self.static = "static attribute"

    def __getattribute__(self, attribute):
        print("Checking for static attribute")
        return super().__getattribute__(attribute)

    def __getattr__(self, attribute):
        """ If there is no attribute
        i     create it with None value
        """
        print("Checking for dynamic attribute")
        self.attribute = None
        return self.attribute


class StaticAttributes:
    def __getattr__(self, attribute):
        """ Always use AttributeError
              with __getattr__ 
        """
        print("Checking for dynamic attribute")
        raise AttributeError


object = DynamicAttributes()

print("Static attribute:", object.static, "\n")

print("Dynamic attribute:", object.dynamic, "\n")

object_2 = StaticAttributes()

try:
    object_2.dynamic
except AttributeError:
    print("Cannot read dynamic attribute from", f"{object_2=}".split("=")[0], "\n")


# Both static and dynamic attributes
#	could be accessed with getattr()
#	Syntax:
#		getattr(<object>, <attribute_name>, <default_value>)
#
# getattr() catches AttributeError, that's
#	why it should be raised when __getattr__
#	is overwriten

static, dynamic = getattr(object, "static", "No static attribute"), getattr(
    object_2, "dynamic", "No dynamic attribute")

print(" getattr() static result:", static)
print("getattr() dynamic result:", dynamic)

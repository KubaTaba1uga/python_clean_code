"""
        Using public attribute name with setattr method
              will lead to infinite recursion as setattr uses
              __set__ method. To avoid the issue, use
              assignment by object.__dict__ or use private
              attributes.
"""


class GoodPublicAttributeDescriptor:
    def __set_name__(self, instance_class, public_name):
        self.public_name = public_name

    def __get__(self, instance, instance_class):
        return instance.__dict__[self.public_name]

    def __set__(self, instance, value):
        instance.__dict__[self.public_name] = value


class BadPublicAttributeDescriptor(GoodPublicAttributeDescriptor):
    def __set__(self, instance, value):
        setattr(instance, self.public_name, value)


class PrivateAttributeDescriptor:
    def __set_name__(self, instance_class, public_name):
        self.private_name = "_" + public_name

    def __get__(self, instance, instance_class):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)


class GoodClient:
    descriptor_public = GoodPublicAttributeDescriptor()
    descriptor_private = PrivateAttributeDescriptor()


class BadClient:
    descriptor = BadPublicAttributeDescriptor()


good_client = GoodClient()

print(f"{good_client.__dict__=}")

good_client.descriptor_public = "123"
good_client.descriptor_private = "098"

print(f"{good_client.__dict__=}")

bad_client = BadClient()

print("{bad_client.__dict__=}")
bad_client.descriptor = "123"

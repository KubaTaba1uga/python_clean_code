"""
        __get__(self, instance, instance_class)  method is called
                 every time attribute is accesed.

        There are two possible scenarious when it happens:

                1. from class instance

                2. from class dicrectly

       Second method argument is related to 1. scenario.
       Third method argument is related to 2. scenario.

        Situations when __get__ is declared without __set__
                method should be avoided, because assigning
                value to descriptor will overwrite it !!!
"""


class DescriptorExample:
    def __get__(self, instance, instance_class):
        if instance is None:
            return self

        return instance


class Client:
    descriptor = DescriptorExample()

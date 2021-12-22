"""
        Multiple inheritance should be used for Mixins or Inheritance Injections.

        Multiple inheritance order is read from top to bottom,
                it is possible thanks to linearization of all classes
                involved into inheritance.
                Use help to check inheritance line.
                      Example:
                                help (BA)

                                Help on class BA in module __main__:

                                                class BA(B, A)
                                                 |  Method resolution order:
                                                 |      BA
                                                 |      B
                                                 |      A
                                                 |      Top
                                                 |      builtins.object

        When interpreter is looking for attribute or method, 
                it makes list of all objects in order. 
               Child (class who inherit others) is always checked first. 

        Multiple inheritance order could be shown also using <class>.mro().
"""


class Top:
    module_name = "module Top"

    def __repr__(self):
        return self.module_name


class A(Top):
    module_name = "module A"


class B(Top):
    module_name = "module B"


class AB(A, B):
    pass


class BA(B, A):
    pass


print("A+B:", AB(), end="\n" * 2)
print("B+A:", BA(), end="\n" * 2)

print("Inheritance order AB:", AB.mro())

print("Inheritance order BA:", BA.mro())

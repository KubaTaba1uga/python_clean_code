"""
        Multiple inheritance should be used for Mixins.

        Multiple inheritance order is read from left to right,
                so class mostly on the left is first, when interpreter
                is looking for attribute or method. If it finds match,
                it is not searching further (interpreter).

        Multiple inheritance order could be shown using <class>.mro().
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

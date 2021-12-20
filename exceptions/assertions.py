"""
     Assertions are to be used for situations that should never happen,
        so the expression on the assert, should indicate software bug as
        critical as there is no recovery from it. Program will no longer
        work after assert statement, as it's logic won't perform desired task.

     Do not TRY/EXCEPT AssertionError!!! NEVER!!!
"""


class AssertionExample:
    def __init__(self):
        self._a = 5
        self._b = 1

    def make_calc(self):
        # Test for impossible situation
        assert (
            self._b != 0
        ), "AssertionExample._b has been changed to 0, during previous calculations"

        return self._a / self._b


example = AssertionExample()
# If some part of code can change
#    example._b to zero (substraction?)
#   maybe it would be good to stop program
#   before the division happens
example._b = 0

example.make_calc()

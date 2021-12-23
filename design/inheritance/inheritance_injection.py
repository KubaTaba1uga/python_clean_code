"""
        Inheritance injection should be used, when want to change 
            inheritance chain, without changing base class.
"""


# Object is required for creating class hierarchy
class UnhealthyDoughFactory(object):
    # Class we want to change
    def get_dough(self):
        return "wheat dough"


class HealthyDoughFactory(object):
    # Class we want change for
    #     without changing a Pizza
    #     inheritance chain
    def get_dough(self):
        return "organic dough"


class Pizza(UnhealthyDoughFactory):
    def order_pizza(self, *ingredients):
        print("Getting dough")

        dough = super().get_dough()

        print("Making pie with", dough)

        for ingredient in ingredients:
            print("Adding:", ingredient)


if __name__ == "__main__":
    Pizza.order_pizza("pepperoni", "mozarella")

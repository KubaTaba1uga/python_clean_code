"""
        Dependency Incection is adding dependencies dynamically
                based on requirements changes.

        Dependency injection should be used, when there is a need 
            to change method resolution order, without changing a base class.
"""


class UnhealthyDoughFactory:
    # Class we want to change
    def get_dough(self):
        return "wheat dough"


class HealthyDoughFactory(UnhealthyDoughFactory):
    # Class we want change for
    #     without changing a Pizza
    #     method resolution order
    def get_dough(self):
        return "organic dough"


class Pizza(UnhealthyDoughFactory):
    """
    Method resolution order:
          |      Pizza
          |      UnhealthyDoughFactory
          |      builtins.object
    """

    def order_pizza(self, *ingredients):
        print("Getting dough")

        dough = super().get_dough()

        print("Making pie with", dough)

        for ingredient in ingredients:
            print("Adding:", ingredient)


class HealthyPizza(Pizza, HealthyDoughFactory):
    """
    Inject dependency into method resolution order.
            Method resolution order:
                   |      HealthyPizza
                   |      Pizza
                   |      HealthyDoughFactory
                   |      UnhealthyDoughFactory
                   |      builtins.object
    """

    pass


if __name__ == "__main__":
    Pizza().order_pizza("pepperoni", "mozarella")
    HealthyPizza().order_pizza("ham", "pineapple")

"""
    Each software element (class, function ...) should be as 
        independent as possible. By minimazing site effects
        software components will be easier to change, because
        logic change in one of them, won't require changing the others.
"""


def calculate_price(base_price: float, tax: float, discount: float) -> float:
    return (base_price * (1 + tax)) * (1 - discount)


def price_formatter_USA(price: float) -> str:
    return "{0:,.2f} $".format(price)


def create_final_price(
    base_price: float, tax: float, discount: float, price_formatter=str
) -> str:
    # Price calculation is independet on its representation,
    #    so changing each won't affect the other
    return price_formatter(calculate_price(base_price, tax, discount))


BASE_PRICE = 99.99

TAX = 0.23

DISCOUNT = 0.1

final_price = create_final_price(BASE_PRICE, TAX, DISCOUNT)

print("Price with default formatter:", final_price)

final_price_USA = create_final_price(BASE_PRICE, TAX, DISCOUNT, price_formatter_USA)

print("Price with USA formatter:", final_price_USA)

import logging


# Don't leave empty
#  except blogs

# Bad logging
try:
    5 / 0
except ZeroDivisionError:
    pass

# Good logging
try:
    5 / 0
except ZeroDivisionError as e:
    logging.error(e)


# Always include orginal Exception
#   in case of exceptions changing

# Bad logging
def bad_function(optional: dict = None):
    try:
        print(optional["VALUE"])
    except TypeError:
        raise KeyError("No `VALUE` key in dictionary")


# Good logging
def good_function(optional: dict = None):
    try:
        print(optional["VALUE"])
    except TypeError as e:
        raise KeyError("No `VALUE` key in dictionary") from e


try:
    good_function()
except KeyError as e:
    # Orginal error can be accessed
    #    via __cause__ attribute
    logging.error((e, e.__cause__))

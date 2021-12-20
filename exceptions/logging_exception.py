import logging

# Good logging
try:
        5/0
except ZeroDivisionError as e:
        logging.error(e)


# Don't leave empty
#  except blogs

# Bad logging
try:
        5/0
except ZeroDivisionError:
        pass

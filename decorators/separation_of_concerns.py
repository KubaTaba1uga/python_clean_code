"""
        Following first SOLID principle:
                Single Responsibility Principle (SRP)

        Decorators should be as small as possible.

        Order in which decorators are applied is important!!!
"""
from functools import wraps
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

# Lets create decorator which will measure
#       function execution time

# Bad design
# Decorator inform about execution start
#       and about time it took, so it is resp-
#       onsible for two actions (SRP violations)
def measure_time(function):
    """Measure time of function execution"""

    @wraps(function)
    def wrapped(*args, **kwargs):
        start_time = datetime.now()

        logging.info("Execution of %s started at %s" % (function.__name__, start_time))

        result = function(*args, **kwargs)

        logging.info(
            "Execution took %r microseconds"
            % (datetime.now() - start_time).microseconds
        )

        return result

    return wrapped


def make_calculations():
    return 9999999999999999999999999999999999 ** 99999


@measure_time
def bad_measure_time():
    make_calculations()


# Good design
# SRP is obeyed
def log_execution_start(function):
    @wraps(function)
    def wrapped(*args, **kwargs):

        logging.info(
            "Execution of %s started at %s" % (function.__name__, datetime.now())
        )

        return function(*args, **kwargs)

    return wrapped


def log_execution_duration(function):
    @wraps(function)
    def wrapped(*args, **kwargs):

        start_time = datetime.now()

        result = function(*args, **kwargs)
        logging.info(
            "Execution took %r microseconds"
            % (datetime.now() - start_time).microseconds
        )

        return result

    return wrapped


@log_execution_start
@log_execution_duration
def good_measure_time():
    make_calculations()

"""
        Decorator changes function behaviour without changing
                its implementation.

        Decorator should be used for:
                1. Transforming parameters
                2. Encapsulate parameters
                3. Tracing code: logging behaviour
                4. Validate parameters
                5. Implement retry logic
                6. Simplify code by moving
                        repetitive parts into decorators


        ALWAYS USE @functools.wraps IN WRAPPED FUNCTION!!!
                It keep docstrings and name of function.
"""
from time import sleep
import functools

# Lets create decorator which will
#       retry any function 3 times if
#       it is failing
def retry(function):
    RETRY_N_TIMES = 3

    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        for _ in range(RETRY_N_TIMES):
            try:
                return function(*args, **kwargs)

            except Exception as e:
                error = e

        raise error

    return wrapped


def error_prone_func():
    print("Executing error_prone_func")
    sleep(2)
    raise RuntimeError


# Use decorator manually
manually_decorated = retry(error_prone_func)

try:
    result = manually_decorated()
except RuntimeError:
    print("error_prone_func failed")


# Use decorator using @<decorator> syntax
@retry
def error_prone_func_0():
    print("Executing error_prone_func_0")
    sleep(3)
    raise RuntimeError


error_prone_func_0()

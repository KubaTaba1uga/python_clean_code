"""
        Creating function decorator  with arguments require
                one more level of nesting. Minimum nesting level
                is 3. First function takes arguments, second and
                third are performing decorator logic.

        ALWAYS USE @functools.wraps IN WRAPPED FUNCTION!!!
                It keep docstrings and name of function.
"""
from time import sleep
import functools

# Lets create decorator which will
#       retry any function N times

# Least nested function takes
#      decorator arguments
def retry(retry_n_times=3):
    # Mid nested function behaves
    #   as decorator
    def nested_function(function):
        @functools.wraps(function)
        def wrapped(*args, **kwargs):
            for _ in range(retry_n_times):
                try:
                    return function(*args, **kwargs)

                except Exception as e:
                    error = e

            raise error

        return wrapped

    return nested_function


@retry(retry_n_times=5)
def error_prone_func():
    print("Executing error_prone_func")
    sleep(2)
    raise RuntimeError


# Creating decorator with parameters require
#       adding parantheses even if there are
#       no arguments passed
@retry()
def error_prone_func_0():
    print("Executing error_prone_func_0")
    sleep(3)
    raise RuntimeError


try:
    error_prone_func()
except RuntimeError:
    print("Executing error_prone_func has failed")

error_prone_func_0()

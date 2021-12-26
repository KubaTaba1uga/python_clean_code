"""
        Creating class decorator with arguments require
                passing arguments into __init__ method, in
                __call__ method arguments are utilized as
                in function decorator without arguments.

        Creating class decorators with arguments is more
                Pythonic, because of better readibility (explicit
                is better than implicit).

        ALWAYS USE @functools.wraps IN WRAPPED FUNCTION!!!
                It keep docstrings and name of function.
"""
from time import sleep
import functools

# Lets create decorator which will
#       retry any function N times


class Retry:
    """Retry function"""

    def __init__(self, retry_n_times):
        self.retry_n_times = retry_n_times

    def __call__(self, function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):

            for _ in range(self.retry_n_times):
                try:
                    return function(*args, **kwargs)

                except Exception as error:
                    func_error = error

            raise func_error

        return wrapper


@Retry(retry_n_times=2)
def error_prone_func():
    """Function that raise RuntimeError"""
    print("Executing error_prone_func")
    sleep(2)
    raise RuntimeError


error_prone_func()

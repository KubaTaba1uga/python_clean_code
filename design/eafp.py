"""
        EAFP - Easier for Forgivness than for Permission

        Perform action directly and care of consequences later,
            it is a philosophy that Python was written in mind.
"""
import logging

try:
    # Perform action directly
    with open("non exsisting file") as file:
        pass
except FileNotFoundError as e:
    # Worry of consequences later
    logging.error(e)

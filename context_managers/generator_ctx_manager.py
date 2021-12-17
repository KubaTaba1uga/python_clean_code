"""
    Generators are prefered way to use context manager 
"""
from enum import Enum

import contextlib


class Mode(Enum):
    READ = 'r'
    APPEND = 'a'
    WRITE = 'w'
    CREATE = 'x'


@contextlib.contextmanager
def file_manager(mode: Mode):
    file = open("test_file", mode.value)
    yield file
    file.close()


# Context managers has to be used
#  using with keywoard
print("1. Write to a file\n")
with file_manager(Mode.WRITE) as file:
    file.write("TEST")

print("2. Read from a file\n")
with file_manager(Mode.READ) as file:
    print("File content:", file.read())

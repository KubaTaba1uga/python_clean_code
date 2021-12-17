"""
    Context managers are useful, when want to:
          1. run precondition
          2. run code
          3. run postcondition
"""
from enum import Enum


class Mode(Enum):
    READ = 'r'
    APPEND = 'a'
    WRITE = 'w'
    CREATE = 'x'


class FileManager:

    def __init__(self, mode: Mode):
        self.mode = mode

    def __enter__(self):
        print("Opening a file")

        self.file = open("test_file", self.mode.value)

        return self.file

    def __exit__(self, exc_type, exc_value, exc_tryceback):
        print("Closing a file")

        self.file.close()


# Context managers has to be used
#  using with keywoard
print("1. Write to a file\n")
with FileManager(Mode.WRITE) as file:
    file.write("TEST")

print("\n2. Read from a file\n")
with FileManager(Mode.READ) as file:
    print("File content:", file.read())

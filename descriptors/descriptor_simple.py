"""
        Descriptors let customize object attribute:
                1. lookup
                2. storage
                3. deletion
"""
import os, logging

logging.basicConfig(level=logging.INFO)

# Static Lookup example
class Ten:
    def __get__(self, instance, instance_class=None):
        return 10


# Each descriptors is assemble from
#       client class and descriptor class
#       (descriptor class has to be clients
#       class attribute)

# Value of 'y' is computed on demand
class TenClient:
    x = 5
    # Ten is client class attribute
    y = Ten()


# Dynamic Lookup example
class DirectoryCounter:
    def __get__(self, instance, instance_class=None):
        return len(os.listdir(instance.path))


# Value of 'items_number' is computed on demand
class CountDirectoryItems:
    # DirectoryCounter is client class attribute
    items_number = DirectoryCounter()

    def __init__(self, path: str):
        self.path = path


github_folder = CountDirectoryItems("/Users/taba1uga/Github/")

print(f" Path: {github_folder.path}\nItems: {github_folder.items_number}")

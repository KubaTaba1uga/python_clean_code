"""
        Built in types shouldn't be extended as their behaviour
             will be different from expected.

             Example:
                extending list and overriding __getitem__
                won't be visible as the method won't be executed
                at all. That's because methods of the class don't
                call each other as expected.

             Solution:
                always use collections objects in such case
"""
from collections import UserList


class BadList(list):

    def __getitem__(self, index):
        value = super().__getitem__(index)
        print("Method executed")
        return value


class GoodList(UserList):

    def __getitem__(self, index):
        value = super().__getitem__(index)
        print("Method executed")
        return value


print("BadList behaviour")
my_list = BadList((1, 2, 3))

print(my_list)

for i in my_list:
    print(i)

# Only here __getitem__ is used
print(my_list[2])

print("\nGoodList behaviour")

my_list = GoodList((1, 2, 3))

print(my_list)

for i in my_list:
    print(i)

# Only here __getitem__ is used
print(my_list[2])

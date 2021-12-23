"""
    Changing arguments inside a function is considered
        a side effect and in most cases should be avoided
        (if there is a reason for it, please document it in
        docstring). If mutable object is passed, use object copy
        in place of orginal.
"""


# Bad function
def bad_multiply_list(orginal_list, multiplier):
    for i, element in enumerate(orginal_list):
        orginal_list[i] = element * multiplier
    return orginal_list


# Good function
def good_multiply_list(orginal_list, multiplier):
    new_list = orginal_list.copy()
    for i, element in enumerate(new_list):
        new_list[i] = element * multiplier
    return new_list


my_list, my_list_0 = [1, 2, 3], [1, 2, 3]

my_multiplier = 5

multiplied_list = bad_multiply_list(my_list, my_multiplier)

print("Bad function:")

print("Multiplied list", multiplied_list)

print("Orginal list", my_list, end="\n" * 2)

multiplied_list = good_multiply_list(my_list_0, my_multiplier)

print("Good function:")

print("Multiplied list", multiplied_list)

print("Orginal list", my_list_0, end="\n" * 2)

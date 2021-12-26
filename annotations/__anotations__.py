def sum_numbers(numbers: list[int]) -> int:
    """Add all numbers in a list"""
    return sum(numbers)


result = sum_numbers([1, 2, 3])

print(" " * 4, "Function result:", result)

print("Function annotations:", sum_numbers.__annotations__)

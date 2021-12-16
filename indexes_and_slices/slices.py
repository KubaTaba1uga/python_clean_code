list = [i for i in range(10)]
start = 3
end = 10
step = 3
# Slices can be used in index notation
#     [start_at :end_at : step]
print("Index notation:", list[start:end:step])

# Slices can also be declare explicitly
#     slice(start_at, end_at, step)
interval = slice(start, end, step)

print("Object notation:", list[interval])

# If one of elements is missing it is cons-
#    idered as None
interval = slice(start, end)

print("Are equal?", list[interval] == list[start: end])

print("IndexError", list[10: 100: 2])

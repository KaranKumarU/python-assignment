# 3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
# list after removing all duplicate values with original order reserved.
# Hint: Use set() to store a number of values without duplicates.

original_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_list = list(set(original_list))

reversed_list = sorted(unique_list, reverse=True)

print(reversed_list)

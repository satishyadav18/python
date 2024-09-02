# Sample list
my_list = [10, 5, 8, 20, 15]

# Find the maximum and minimum values along with their indices
max_value, max_index = max((val, idx) for idx, val in enumerate(my_list))
min_value, min_index = min((val, idx) for idx, val in enumerate(my_list))

# Print the results
print("Maximum Value:", max_value)
print("Index of Maximum Value:", max_index)

print("Minimum Value:", min_value)
print("Index of Minimum Value:", min_index)

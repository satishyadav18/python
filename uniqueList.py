'''Write a Python function that takes a list and returns a new list with unique elements
of the first list.
Sample List : [1,2,3,3,3,4,3,5]
Unique List : [1, 2, 3, 4, 5]'''

sample_input = input("Enter a list of numbers separated by spaces: ")

# Converting the input string into a list of integers
sample_list = [int(num) for num in sample_input.split()]

unique_list = list(set(sample_list))

print(f"Original List: {sample_list}")
print(f"Unique List: {unique_list}")

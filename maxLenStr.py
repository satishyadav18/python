# Take a list of strings as input
str_list = input("Enter a list of strings (comma-separated): ").split(',')

# Find the length of the longest string
max_length = max(len(s) for s in str_list)

print(f"The length of the longest string in the list: {max_length}")

input_string = input("Enter a string: ")

# Check if all characters in the string are '0' or '1'
is_binary = all(char in '01' for char in input_string)

if is_binary:
    print("The given string is a binary string.")
else:
    print("The given string is not a binary string.")

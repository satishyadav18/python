'''B) Remove all duplicates characters from a given string in Python
Examples:
Input : abcabcde
Output : abcde '''

user_input = input("Enter a string: ")
unique_char = set()
result_str = ""

for char in user_input:
    if char not in unique_char:
        unique_char.add(char)
        result_str = result_str + char

print(f"Original string: {user_input}")
print(f"Resulted string : {result_str}")
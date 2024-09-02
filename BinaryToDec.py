binary_input = input("Enter a binary number: ")
decimal_num = 0
binary_str = str(binary_input)

for i in range(len(binary_str) -1, -1, -1):
    if binary_str[i] == '1':
        decimal_num = decimal_num + 2**(len(binary_str) - 1 -i)
    
print(f"The decimal equivalent of {binary_str} is {decimal_num}")
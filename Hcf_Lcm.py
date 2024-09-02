# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating HCF
x, y = num1, num2
while y:
    x, y = y, x % y
hcf_result = x

# Calculating LCM
lcm_result = (num1 * num2) // hcf_result

# Printing the results
print(f"HCF of {num1} and {num2} is: {hcf_result}")
print(f"LCM of {num1} and {num2} is: {lcm_result}")

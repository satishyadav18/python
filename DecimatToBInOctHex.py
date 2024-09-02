decimal_number = int(input("Enter a decimal number: "))
base = int(input("Enter the base (2, 8, 16, etc.): "))

result = ""

while decimal_number > 0:
    quotient, remainder = divmod(decimal_number, base)
    result = str(remainder) + result
    decimal_number = quotient

print(f"The equivalent number in base {base}: {result}")

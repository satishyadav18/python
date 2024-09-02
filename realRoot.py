import math

# Take user input for coefficients a, b, and c
a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is non-negative
if discriminant >= 0:
    # Calculate the roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    # Print the roots
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    print("The roots are complex and cannot be calculated with this script.")

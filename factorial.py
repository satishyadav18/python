n=int(input("Enter number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of the number is: ")
print(fact)


'''def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Taking input from the user
number = int(input("Enter a number: "))

# Calculating and displaying the factorial
result = factorial_recursive(number)
print(f"The factorial of {number} is {result}") '''

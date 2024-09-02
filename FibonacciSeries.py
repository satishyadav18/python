# Take user input for the number of terms
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Initialize the first two terms
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

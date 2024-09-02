# Write a Python script to print all Prime numbers between 1 to n.# Check if a number is prime
def is_prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    return count == 0

# Take user input for n
n = int(input("Enter the value of n: "))

# Print prime numbers in the range
prime_list = [i for i in range(2, n + 1) if is_prime(i)]
print(f"Prime numbers in the range: {prime_list}")

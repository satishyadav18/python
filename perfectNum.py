# Example usage:

num = int(input("Enter a number: "))

# Check for valid input (positive integer)
if num <= 0:
    print(f"{num} is not a Perfect number.")
else:
    # Find the proper divisors and calculate their sum
    divisors_sum = sum(divisor for divisor in range(1, num) if num % divisor == 0)

    # Check if the sum of divisors is equal to the original number
    if divisors_sum == num:
        print(f"{num} is a Perfect number.")
    else:
        print(f"{num} is not a Perfect number.")

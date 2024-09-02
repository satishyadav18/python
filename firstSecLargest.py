n = int(input("Enter the value of N: "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

if len(numbers) < 2:
    print("At least two numbers are required.")
else:
    largest = max(numbers)
    numbers.remove(largest)
    second_largest = max(numbers)

    print("Largest number: ", largest)
    print("Second largest number: ", second_largest)
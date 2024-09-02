n = int(input("Enter the value of n: "))
result = 0.0

for i in range(1, n + 1):
    result += 1 / i
result = round(result, 6)
print(f"The value of the series for n = {n}: {result}")

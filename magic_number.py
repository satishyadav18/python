num = int(input("Enter a number: "))

while num > 9:
    sum_of_digits = 0
    while num > 0:
        sum_of_digits =sum_of_digits + num % 10
        num = num // 10
    num = sum_of_digits

if num == 1:
    print("It's a magic number!")
else:
    print("It's not a magic number.")




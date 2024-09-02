# Write a Python program to print every integer between 1 and n divisible by m. Also
# report whether the number that is divisible by m is even or odd.

n = int(input("Enter an integer: "))
m = int(input("Enter m: "))

for i in range(1,n+1):
    if i % m == 0:
        print(f"{i} is divisible by {m}")
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
            

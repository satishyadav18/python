m = int(input("Enter m: "))
n = int(input("Enter n:"))

for num in range(1, n+1):
    if num % m == 0:
        print(f"{num} is divisible by {m}")
        if(num % 2 == 0):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
        #print(f"{num} is {'even' if num % 2 == 0 else 'odd'}")
items = int(input("Enter the no ef items: "))
if items < 10:
    price = items * 120
elif 10 < items < 99:
    price = items * 100
else:
    price = items * 70

print(f"Cost of {items} is {price}")
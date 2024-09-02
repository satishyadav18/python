a =int(input("Enter the first side: "))
b =int(input("Enter the second side: "))
c =int(input("Enter the third side: "))

if a==b==c:
    print("Equilateral triangle")
elif a==b or b==c or c==a:
    print("Isosceles triangle")
else:
    print("Scalane triangle")
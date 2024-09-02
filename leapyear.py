years = int(input("Enter the year: "))

if years % 400 == 0:
    print(f"year {years} in not leap year.")
elif years % 100 == 0:
    print(f"year {years} is not a leap year.")
elif years % 4 == 0:
    print(f"Year {years} is a leap year.")
else:
    print(f"year {years} is not a leap year.")

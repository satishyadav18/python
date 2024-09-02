n = int(input("Enter the value of n: "))
grp_26_35 = 0
grp_36_45 = 0
grp_46_55 =0

for i in range(n):
    age = int(input("Enter employee age: "))

    if 26 <= age <= 35:
        grp_26_35 = grp_26_35 + 1
    elif 36 <= age <= 45:
        grp_36_45 =grp_36_45 + 1
    elif 46 <= age <= 55:
        grp_46_55 = grp_46_55 + 1

print(f"Employee in group 26 - 35: {grp_26_35}")
print(f"Employee in group 36 - 45: {grp_36_45}")
print(f"Employee in group 46 - 55: {grp_46_55}")

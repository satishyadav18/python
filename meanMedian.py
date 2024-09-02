
# Write a python program to find the mean and median of a set of elements.

input_str = input("Enter element separated by spaces: ")
elements = [float(x) for x in input_str.split()]

if not elements:
    print("No element entered. please enter numerical value")
else:
    mean = sum(elements) / len(elements)

    sorted_ele = sorted(elements)
    n = len(sorted_ele)

    if n % 2 == 0:
        mid1 =sorted_ele[n // 2 - 1]
        mid2 = sorted_ele[n // 2]
        median = (mid1+mid2) / 2
    else:
        median = sorted_ele[n // 2]

    print(f"Mean:{mean}")
    print(f"Medain:{median}")


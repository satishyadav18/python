rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end=" ")

    # Print increasing numbers
    for k in range(1, i + 1):
        print(k, end=" ")

    # Print decreasing numbers
    for l in range(i - 1, 0, -1):
        print(l, end=" ")

    # Move to the next line for the next row
    print()

'''Print the following pattern using Python program
1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1
64 32 16 8 4 2 1
'''

rows = int(input("Enter the no. of rows: "))

for i in range(rows):
    num = 2 ** i
    for j in range(i+1):
        print(num, end = " ")
        num = num // 2
    print()
# Get user input for N (greater than 20)
while True:
    N = int(input("Enter a number greater than 20 (N): "))
    if N > 20:
        break
    else:
        print("Please enter a number greater than 20.")

# Print numbers from 11 to N with conditions
for num in range(11, N + 1):
    output = ""
    
    if num % 3 == 0:
        output = "Tipsy"
    
    if num % 7 == 0:
        output = "Topsy"
    
    if not output:
        output = num
    
    print(output)

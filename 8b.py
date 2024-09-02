# Write a short program to find the average of some numbers entered.

num = []
while True:
    user_input = input("Enter the number: (press 'q' to see result.)")
    
    if user_input.lower() == 'q':
        break
    num.append(int(user_input))
if len(num) != 0:
    avg = sum(num) / len(num)
    print("average is", avg )
else: 
    print("invalid input.")
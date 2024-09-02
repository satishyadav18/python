
numbers = []
while True:
    user_input = input("Enetr 'q' to see average..")
    
    if user_input.lower() == 'q':
        break
    numbers.append(int(user_input))
if len(numbers) != 0:   
   
    print("Average is: ", sum(numbers) / len(numbers))
else:
    print("Average is 0.0")

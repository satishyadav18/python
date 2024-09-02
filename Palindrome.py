print("Enter numbers: (Enter 'q' to stop)")

while True:
    user_input = input()

    if user_input.lower() == 'q':
        break

    num = int(user_input)
    
    if str(num) == str(num)[::-1]:
        print(f"{num} is a Palindrome Number")
    else:
        print(f"{num} is not a Palindrome Number")

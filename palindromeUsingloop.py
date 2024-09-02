palindromes = []

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
  
    if user_input.lower() == 'q':
        break

    if user_input.isdigit():
        number = int(user_input)
        if str(number) == str(number)[::-1]:
            palindromes.append(number)
        else:
            print("Invalis input.")
        
if palindromes:
    print("Palindrome number: ", palindromes)
else:
    print("No palnidrome numbers were entered.")
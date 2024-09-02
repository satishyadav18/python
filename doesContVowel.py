str = input("Enter a string: ")
lower_str = str.lower()

if all(char in lower_str for char in 'aeiou'):
    print("The string conatain all vowels.")
else:
    print("The string doesn't contain all vowels.")
    
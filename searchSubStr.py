string = input("Enter a string: ")
search_sstr = "Emma"

last_position = string.rfind(search_sstr)

if last_position != -1:
    print(f"The last position of '{search_sstr}' in given string is: {last_position}.")
else:
    print(f"The substring '{search_sstr}' is not found in given string. ")




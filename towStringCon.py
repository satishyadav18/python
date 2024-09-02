#i.Take a string of length greater than 2, return a string except 1 st and last characters.
'''
input_str = input("Enter string: ")

if len(input_str) > 2:
    result_str = input_str[1:-1]
    print(result_str)
else:
    print("Input string should be of length greater than 2.")'''
  
# Take 2 strings, s1, and s2 return a new string made of the first, middle and last
# char of each input string.

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1) > 0 and len(s2) > 0:
    result_str = s1[0] + s1[len(s1)//2] + s1[-1] + s2[0] + s2[len(s2)//2] + s2[-1]
    print(result_str)

else:
    print("both input strings should have at least one character. ")

# Write a python program to take 2 strings, s1 and s2, create a new string by
# appending s2 in the middle of s1.
'''
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

mid_idx = len(s1) // 2
 
result_str = s1[:mid_idx] + s2 + s1[mid_idx:]
print("Resulting stirng:", result_str) '''
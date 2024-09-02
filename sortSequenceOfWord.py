
input_sequence = input("Enter a hyphen-separated sequence of words: ")

# Split the input sequence into a list of words
words = input_sequence.split('-')

# Sort the list alphabetically
sorted_words = sorted(words)

# Join the sorted words back into a hyphen-separated sequence
output_sequence = '-'.join(sorted_words)

print("Output:", output_sequence)

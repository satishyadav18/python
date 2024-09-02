digit = int(input("Enter a digit (0-9): "))
if 0 <= digit <= 9:
    words = ["Zero","one","Two","Three","Four","five","Six","Seven","Eight","Nine"]
    print(words[digit])
else:
    print("Invalid input")
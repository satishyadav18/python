hr = int(input("Enter the hour between 1-12: "))
n = int(input("Enter the no. of hours ahead: "))

s = hr + n

if s > 12:
    s = s-12

print("Time at that time would be:",s,"O'clock") 



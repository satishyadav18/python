num=int(input("Enter the number to reversed: "))

rev_num=0

while(num>0):
    rem=num%10
    rev_num=rev_num*10+rem
    num=num//10
print("reversed number is: ",rev_num)




#number=''.join(num[::-1])
#print(number)
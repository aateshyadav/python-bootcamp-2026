""" num=int(input("enter a number:")) #checking number is positive or negative
print(num)

if(num<0):
    print("number is negative")
elif(num>0):
    print("number is positive")
else:
    print("number is zero") """

""" from unittest import case


num=int(input("enter a number : "))  #matching number to day of week

match num:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday") """

""" sum=0   # sum of numbers from 1 to 100
for i in range(1,101):
    sum=sum+i
print(sum) """

""" for i in range(1,6): # printing pattern *,**,***,****,*****
    print("*"*i) """

""" i=1    # printing number using while loop
while(i<11):
    print(i)
    i=i+1 """

""" sum=0   # sum of numbers using while loop
i=1
while(i<51):
    sum=sum+i
    i=i+1
print(sum) """

""" password = int(input("enter the password:"))
while(password!=1234):
    print("wrong password")
    password = int(input("enter the password:"))
print("correct password") """

""" num=45222  # reversing a number
print(int(str(num)[::-1])) """

""" for i in range(1,11):
    print(i)
    if(i==7):
        break """

for i in range(1,11):
    if(i==5):
        continue
    print (i)
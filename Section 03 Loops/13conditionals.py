""" 
age=int(input("enter your age: "))
if(age>18):
    print("you can drive")
    print("thank you")
else:
    print("you cannot drive")
print("end of program")
 """
age=int(input("enter your age: "))
if(age>18):
    print("you can drive")
elif(age==18):
    print("let's schedule your interview")
else:
    print("sorry you cannot drive")
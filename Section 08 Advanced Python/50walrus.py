# Walrus operator was introduced in Python 3.8 and allows you to assign a value to a variable as part of an expression.
def very_slow_func():
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    print("something....")
    return 7

""" a=very_slow_func()  # regular method
if(a>10):
    print(a) """

""" if((a:=very_slow_func())>10):  # walrus method
    print(a)

else:
    print("its not grater than 10") """

while(data:=input("enter the value: ")):
    print(data)
    if data == "q":
        break
    
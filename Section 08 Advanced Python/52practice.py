# 1.Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".
""" def logger(func):
    def wrapper():
        print("function is  being called!")
        func()
    return wrapper 

@logger
def say_hello():
    print("hello")

say_hello() """

# 2. Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.
""" from time import time

def timer(func):
    def wrapper(n):
        t1=time()   # initial time
        result = func(n)     # sum function running
        t2=time()   # final time 
        print(t2-t1)
        return result
    return wrapper

@timer
def sum_1m(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

a=sum_1m(1000000)
print(a) """


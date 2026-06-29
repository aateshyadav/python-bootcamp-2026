# Decorators is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new fucntion

def decorator(func):
    def wrapper():
        print("i am about to execute a function....")
        func()
        print("i have executed this function....")
    return wrapper

def say_hello():    # Method 1 
    print("hello")
f=decorator(say_hello)
f()


@decorator          # Method 2
def say_hello():
    print("hello")
say_hello()
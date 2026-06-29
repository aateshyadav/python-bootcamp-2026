# Fibonacci series 
# 0 1 1 2 3 5 8 13.....
# fib(n)=fib(n-1)+fib(n-2)

def fib(n):
    # base case of recursion
    if(n==0 or n==1):
        return n
    return fib(n-1)+fib(n-2)
print(fib(10)) 

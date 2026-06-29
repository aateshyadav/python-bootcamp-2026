""" def sum_of_digits(n):
    if n==0:
        return 0
    
    return n%10 + sum_of_digits(n//10)
print(sum_of_digits(7532)) """

""" import math
b=math.sin(math.radians(90))
print(b) """

""" import requests

a=requests.get("https://api.github.com/")
print(a.json()) """
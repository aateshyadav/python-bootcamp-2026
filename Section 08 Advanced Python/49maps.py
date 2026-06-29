# MAP
""" numbers=[1,2,3,45,4,21]

#def square(x):
    #return x*x

new=list(map(lambda x:x*x,numbers))
print(new) """

# FILTER
""" def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False  """
"""     
a=[1,3,5,234,34,21,33,223,24,2,4,22,43,27]

new=list(filter(lambda x:x>9,a))
print(new) """

# REDUCE
from functools import reduce
numbers=[1,2,3,4,5,6]

def sum(a,b):
    return a+b

c =  reduce(sum,numbers)
print(c)

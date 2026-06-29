""" def sum(a,b):
    c=a+b
    z=1    # it creates a local variable called z which is called after this fucntion returns 
    return c 

z=8  # z is a global variable
print(z)
print(sum(4,6)) """

# Docstrings 
def sum(a,b):
    """This will sum two numbers"""
    c=a+b
    return c
print(sum.__doc__)

print(sum(2,3))
#finally
a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

try:
    c=a/b
    print(c)

except Exception as e:
    print(e)

# this is always executed no matter if try completely executes or not

finally:   # inside a function print does not work without finally: 
    print("this is always executed")
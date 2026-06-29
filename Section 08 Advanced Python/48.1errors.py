# error handling
""" while True:
    try:
        a = int(input("enter number 1 : "))
        b = int(input("enter number 2 : "))
        print(f"the division is {a/b}")

    except ValueError:
        print("please do not perform bad typecasts")

    except ZeroDivisionError:
        print("hey do not divide by 0")

    except Exception as e:
        print("some error ocurred!",e) """
    

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

if b == 0:
    raise ValueError("Please do not divide by 0")

print(f"the division is {a/b}")

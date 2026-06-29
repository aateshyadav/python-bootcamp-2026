try:
    a=int(input("enter the first number : "))
    b=int(input("enter the second number : "))

    print("what kind of operation do you want to perform.\nPress + for addition\nPress - for subtraction\nPress * for multiplication\nPress/ for division")

    o=input("Enter operation: ")
    match o:
        case "+":
            print(f"the result is: {a+b}")
        case "-":
            print(f"the result is: {a-b}")
        case "*":
            print(f"the result is: {a*b}")
        case "/":
            print(f"the result is: {a/b}")
        case default:
            print(f"there was an error")

except Exception  as e:
    print("enter a valid value of a and b")
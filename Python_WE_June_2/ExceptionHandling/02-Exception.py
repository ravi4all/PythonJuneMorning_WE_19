try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = a + b
    d = a - b
    e = a / b
    f = a * b
except ValueError:
    print("Invalid Input...Please enter a digit from 0-9")
except ZeroDivisionError:
    print("Cannot divide by zero")
except BaseException as ex:
    print(ex)
else:
    print("Sum is", c)
    print("Diff is", d)
    print("Div is", e)
    print("Mul is", f)
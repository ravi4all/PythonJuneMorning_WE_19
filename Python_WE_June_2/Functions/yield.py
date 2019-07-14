def calc(x,y):
    z1 = x + y
    yield z1
    print("Sum is",z1)
    z2 = x - y
    yield z2
    print("Sub is",z2)
    z3 = x / y
    yield z3
    print("Div is",z3)
    z4 = x * y
    yield z4
    print("Mul is",z4)

#x = calc(4,5)
#print(x)

a,b,c,d = list(calc(4,5))
print(a,b,c,d)

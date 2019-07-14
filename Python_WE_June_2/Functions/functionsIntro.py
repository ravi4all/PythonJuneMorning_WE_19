a = 55
b = 21

# function declaration/definition
def add():
    # local variables
    global a
    a = 12
    b = 33
    c = a + b
    print(c)

# function calling
add()

print(f"A is {a} and B is {b}")
z = a - b
print(z)

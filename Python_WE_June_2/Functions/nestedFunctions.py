def calc():
    x = 12
    y = 22
    def add():
        z = x + y
        return z
    def sub():
        z = x - y
        return z

    # print(add())
    # print(sub())
    return add,sub

def main():
    z = calc()
    # print(z)
    print(z[0](), z[1]())

main()
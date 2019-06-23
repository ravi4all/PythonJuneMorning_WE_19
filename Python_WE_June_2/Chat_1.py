name = input("Enter your name : ")
print("Hello",name)

while True:
    msg = input("Enter your message : ")
    if msg == "hello":
        print("Hello",name)
    elif msg == "bye":
        print("Bye {}, See you soon".format(name))
        break
    else:
        print("I don't understand")

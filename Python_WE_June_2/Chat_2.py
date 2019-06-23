name = input("Enter your name : ")
print("Hello",name)

while True:
    msg = input("Enter your message : ")
    #Logical Operator - and, or, not
    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hello",name)
    elif msg == "bye":
        print("Bye {}, See you soon".format(name))
        break
    else:
        print("I don't understand")

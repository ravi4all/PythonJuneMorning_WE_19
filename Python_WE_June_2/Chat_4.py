name = input("Enter your name : ")
print("Hello",name)

helloIntent = ["hi","hello","hey","hi there","hey there","howdy"]

while True:
    msg = input("Enter your message : ")
    #Membership Operator - in, not in
    if msg in helloIntent:
        print("Hello",name)
    elif msg == "bye":
        print("Bye {}, See you soon".format(name))
        break
    else:
        print("I don't understand")

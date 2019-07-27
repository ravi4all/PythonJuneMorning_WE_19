def atm():
    total = 12000
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Welcome User")
    else:
        # print("Invalid PIN")
        raise ValueError("Invalid PIN")

    amt = int(input("Enter amount : "))
    if amt > total:
        # print("Insufficient Balance")
        raise ValueError("Insufficient Balance")
    else:
        total -= amt
        print("Remaining Balance is",total)
    print("Transaction Successful")

try:
    atm()
except ValueError as err:
    print(err)
    atm()
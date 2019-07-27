def atm():
    total = 12000
    pin = input("Enter your PIN : ")
    assert (pin == "1234"),"Invalid PIN"
    print("Welcome User")

    amt = int(input("Enter amount : "))
    assert (amt < total),"Insufficient Balance"
    total -= amt
    print("Remaining Balance is",total)
    print("Transaction Successful")

try:
    atm()
except AssertionError as err:
    print(err)
    atm()
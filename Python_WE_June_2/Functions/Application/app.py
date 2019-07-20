users = []
def login():
    email = input("Enter email : ")
    pwd = input("Enter pwd : ")
    # Login User

def register():
    name = input("Enter name : ")
    # Check Email Already Exist or Not
    email = input("Enter email : ")
    pwd = input("Enter pwd : ")
    user = {"name":name, "email":email, "pwd":pwd}
    users.append(user)

def main():
    while True:
        print("""
        1. Login 
        2. Register
        """)
        ch = input("Enter your ch : ")
        todo = {
            "1":login,
            "2":register
        }
        todo.get(ch)()

main()
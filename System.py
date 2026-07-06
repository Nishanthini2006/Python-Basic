user = input("Username: ")
pin = int(input("PIN: "))
if user == "admin":
    if pin == 1234:
        print("Login Success")
    else:
        print("Wrong PIN")
else:
    print("Wrong Username")

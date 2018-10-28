print("Hi there, this is a superuser gateway")
superuser = "c4e"
pwd = "codethechange"
username = input("Username: ")
while username != superuser:
    print("You are not superuser!")
    username = input("Username: ")
else:
    password = input("Password: ")
    while password != pwd:
        print("Password is incorrect!")
        password = input("Password: ")
    else:
        print("Welcome, c4e!")

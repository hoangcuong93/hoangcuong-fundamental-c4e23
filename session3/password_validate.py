pwd = input("enter your pass: ")

while (len(pwd) <= 8) or pwd.isalpha() or (pwd.isupper()) or (pwd.islower()) or pwd.isdigit:
    print("not ok")
    if len(pwd) <= 8:
        print("pass ngan qua")
    if pwd.isalpha:
        print("nhap so")
    if pwd.isupper() or pwd.islower():
        print("dasdasdas")
    if pwd.isdigit:
        print("12131231")
    pwd = input("enter your pass: ")
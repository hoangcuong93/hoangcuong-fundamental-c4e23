yob_str = input("nam sinh: ")
while not yob_str.isdigit():
    print("not ok")
    yob_str = input("nam sinh: ")
yob = int(yob_str)
age = 2018 - yob
print(age)

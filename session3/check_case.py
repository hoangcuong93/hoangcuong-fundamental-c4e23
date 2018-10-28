s = input("enter a text: ")
if (not s.isdigit()) and (not s.islower()) and (not s.isupper()):
    print("ok")
else:
    print("not ok")

shop_list = ["T-shirt", "Sweater"]

while True:
    a = (input("Welcome to our shop. What do you want (C, R, U, D)?: ").upper())

    if a.upper() == "C":
        shop_list.append(input("What item you want to add? ").upper())
    elif a.upper() == "U":
        i = int(input("Which position you want to update? "))
        shop_list[i-1] = input("New item? ")
    elif a.upper() == "D":
        n = int(input("What position do you want to delete? "))
        shop_list.pop(n-1)
    elif a.upper() == "R":
        pass
    else: 
        print("Please enter the correct (C, R, U, D) ")
    print("Our items: ", end="")
    print(*shop_list, sep="," )
   
    

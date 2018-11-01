dic = {
    "nyc": "nguoi yeu cu",
    "hc": "hoc",
    "lm": "lam",
}
while True:
    key = input("teen dic: ")
    if key in dic:
        print(dic[key])
    else:
        key2 = input("not found, new teen dic? (Y/N): ").upper()
        if key2 == "Y":
            trans = input("your trans: ")
            dic[key] = trans


    

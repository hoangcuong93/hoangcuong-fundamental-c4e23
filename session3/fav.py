favs = ["neftlix", "redbull"]
print(*favs, sep=", ")
newitem = input("new fav: ")
favs.append(newitem)
print(*favs, sep=", ")
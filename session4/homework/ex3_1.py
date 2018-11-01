pr = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
st = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0
for i in st:
    print(i)
    print("price: ", pr[i])
    print("stock: ", st[i])
    m = pr[i] * st[i]
    total += m
print(total)
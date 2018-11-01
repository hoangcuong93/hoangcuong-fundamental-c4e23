# person = ["H.Cuong", "Nam Dinh", "UFM", 25, 4, 257, False]
# person = {}
# print(person)
# print(type(person))

person = {
    "name": "H.Cuong",
    "location": "Nam Dinh",
    "age": 25,
}

print(person)
person["friend_count"] = 257
print(person)
key = "name"

print(person[key])
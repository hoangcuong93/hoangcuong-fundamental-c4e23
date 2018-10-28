# item1 = "pho bo"
# item2 = "so huyet"
# item3 = "bun vit"
# item4 = "chao"
# item5 = "com rang"

# items = [] # empty list
# print(items)
# print(type(items))
items = ["chao", "so huyet", "bun vit"]
i = int(input("index "))
new_value = input("new value")
items [i] = new_value
# print(items)
# items.pop(1)
print(items)
items.remove("so huyet")
print(items)
a = ["If x = 8, then what is the value of 4(x+3)?", 35, 36, 40, 44]
b = ["Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is his approximate average score?", 55, 65, 75, 85]

count =0

for i in range(1, 5):
    print(i, a[i], sep =". ")

y = int(input("number: "))
if y == 4 or y == 44:
    print("ok!")
    count += 1
else:
    print("failed!")

print()
for i in range(1, 5):
    print(i, b[i], sep =". ")

n = int(input("number: "))
if n == 2 or n == 65:
    print("ok!")
    count += 1
else:
    print("failed!")

print("You've answered correctly", count, "out of 2 quessions")
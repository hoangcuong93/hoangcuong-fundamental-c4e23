a = [35, 36, 40, 44]

print("Answer the following algebra question: ")
print("if x = 8, then what is the value of 4(x + 3) ?")

for i, v in enumerate(a):
    print(i + 1, v, sep = ". ")

n = int(input("Your choice: "))
if n == 4 or n == 44:
    print("ok")
else:
    print("failed!")
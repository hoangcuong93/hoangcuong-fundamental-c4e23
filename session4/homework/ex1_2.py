s = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is C and these are my sheep sizes: ", s)
print("Now my biggest sheep has size", max(s), "lets shear it")
s[s.index(max(s))] = 8
print("After shearing, here is my flock", s)

a = int(input("Month: "))
for i in range(a):
    print("Month", i+1)
    for v in range(len(s)):
        s[v] += 50
    print("One month has passed, now here is my flock: ", s)
    if i+1 == a:
        break
    print("Now my biggest sheep has size", max(s), "lets shear it")
    s[s.index(max(s))] = 8
    print("After shearing, here is my flock", s)

total = 0
for i in s:
    total += i
print("My flock has size in total: ", total)
print("I would get:", total, "* 2$ =", total * 2, "$")

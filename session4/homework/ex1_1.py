s = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is C and these are my sheep sizes: ", s)

a = int(input("Month: "))
for i in range(a):
    print("Month", i+1)
    for x in range(len(s)):
        s[x] += 50
    print("One month has passed, now here is my flock: ", s)
    print("Now my biggest sheep has size", max(s), "lets shear it")
    s[s.index(max(s))] = 8
    print("After shearing, here is my flock", s)

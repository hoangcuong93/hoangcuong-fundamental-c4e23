m1 = {'name': 'quan',
'hour': 30,
'vnd.per.hour': 50 }
m2 = {'name': 'huy',
'hour': 20,
'vnd.per.hour': 40 }
m3 = {'name': 'duc',
'hour': 15,
'vnd.per.hour': 35 }
m = [m1, m2, m3]
print(m)
s = 0
for i in m:

    print(i['name'], i['hour'], sep=": ")
    print("luong theo tuan cua", i['name'], i['hour'] * i['vnd.per.hour'])
    s += i['hour'] * i['vnd.per.hour']
    
print(s)
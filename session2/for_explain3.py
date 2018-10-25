from turtle import *
speed(0)
s = 10
shape("turtle")
for i in range(50):
    forward(s)
    left(90)
    s = s + 10 # s +=10
mainloop()
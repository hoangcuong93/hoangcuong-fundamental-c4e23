from turtle import *
speed(0)
shape("turtle")
fillcolor('red')
for i in range(3,7):
    if i%2==0 :
        pencolor('red')
    else:
        pencolor('blue')
    n = i 
    for x in range(n):
        forward(150)
        left(360/n)      
mainloop()
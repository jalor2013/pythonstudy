import turtle
import random
'''import random
turtle.colormode(255)
x=0
d=40
turtle.pensize(10)

for i in range(7):
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    turtle.color(r,g,b)
    turtle.left(90)
    turtle.circle(d,180)

    d=d+20
    x=x+20
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()


    turtle.left(90)'''
#
for j in range(12):
    turtle.pendown()
    w=1
    
    for i in range(5):
        turtle.forward(5)
        #turtle.pensize(w)
        w=w+1
        
    turtle.penup()
    turtle.goto(0,0)
    turtle.circle(10,-30)
    
    

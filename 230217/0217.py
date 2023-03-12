import turtle
import random
'''r=int(turtle.numinput('圆形绘制','请输入圆形半径'))
turtle.circle(r)'''
turtle.speed(50)
turtle.pensize(5)
turtle.screensize(bg='black')
turtle.color('white')

turtle.colormode(255)
for j in range(20):
    x=random.randint(-400,400)
    y=random.randint(-400,400)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.color(r,g,b)



    for i in range(6):
        turtle.forward(15)
        turtle.circle(2)
        turtle.circle(-2)
        turtle.forward(10)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.right(60)




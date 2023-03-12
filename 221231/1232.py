import turtle
import random
turtle.speed(50)


#turtle.color('yellow')

turtle.screensize(bg='black')
turtle.pensize(10.10)



a=0
c=0
while a<30:
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    
    c = random.randint(1,5)
    turtle.penup()
    turtle.goto(x,y)
    if c== 1:
      turtle.color('yellow')
    elif c == 2:
      turtle.color('red')
    elif c == 3:
      turtle.color('blue')
    elif c == 5:
      turtle.color('purple')
    else:
      turtle.color('pink')

    
    turtle.pendown()
    for i in range(5):
        turtle.forward(20)
        turtle.right(144)
    a=a+1
turtle.hideturtle() 


    
    
    

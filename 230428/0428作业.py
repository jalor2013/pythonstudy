import turtle

t=turtle


turtle.pencolor('black')
turtle.pensize(2)

t.fillcolor('yellow')
t.begin_fill()

turtle.penup()
turtle.goto(-90,90)
turtle.pendown()
turtle.forward(180)
turtle.goto(-90, -90)
turtle.left(90)
turtle.forward(180)

t.end_fill()

t.fillcolor('red')
t.begin_fill()

t.penup()
turtle.goto(-90,-90)
turtle.pendown()
t.right(90)
t.forward(180)
t.left(90)
t.forward(180)
t.goto(-90,-90)
t.end_fill()
turtle.hideturtle() 



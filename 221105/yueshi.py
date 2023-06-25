import turtle
myPen = turtle.Pen()


turtle.bgpic("sea.gif")

myPen.left(90)
myPen.forward(150)
myPen.pencolor("silver")
myPen.dot(100)

myPen.hideturtle()
myPen.penup()
myPen.right(90)
myPen.backward(100)
myPen.pendown()

myPen.pencolor("black")
myPen.dot(100)
for i in range(100):
    myPen.forward(1)
    myPen.dot(100)

turtle.done()

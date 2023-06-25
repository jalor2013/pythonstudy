'''number = [1, 2.5,"codemao"]
print(number[2])'''






import turtle
myPen = turtle.Pen()
myPen.pensize(20)
Pos = [(0, 0), (260, 0), (130, -110),
       (-130, -110), (-260, 0)]
Colors = ["black", "red", "green",
          "yellow","blue"]
for i in range(5):
    myPen.penup()
    myPen.goto(Pos[i])
    myPen.pendown()
    myPen.pencolor(Colors[i])
    myPen.circle(100)
myPen.hideturtle()
turtle.done




import turtle
import random
pen = turtle.Pen()

turtle.bgpic("转盘.gif")
pen.dot(50,"gold")
pen.pencolor("gold")
pen.fillcolor("gold")
pen.shape("arrow")
pen.shapesize(2,10)

n = random.randint(0,3)
for i in range(20+n):
    pen.right(90)
pen.hideturtle()
pen.clear()


if n == 0:
    turtle.bgpic("跳绳.gif")
elif n == 1:
    turtle.bgpic("篮球.gif")
elif n == 2:
    turtle.bgpic("麦克风.gif")
else:
    turtle.bgpic("玩偶.gif")
turtle.done()

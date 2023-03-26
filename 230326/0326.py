#define:定义  def:用来定义函数的一个指令,可以根据需求创造出新的函数
#创造新函数时,def后面跟的是新函数的名称,被放入新函数里面的代码无法直接执行
#如果要运行新函数,需要直接调用新函数名称
import turtle as t
'''def draw_circle(x,y,r):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)
draw_circle(0,-200,200)
draw_circle(0,-100,100)'''
#做出一个可以在指定坐标画出正方形的自定义函数
def draw_square(x,y,d):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(d)
        t.right(90)
#用drad_square函数做出在随机位置画出

        
import random
t.bgcolor('black')
t.speed(0)
color_list=('blue','yellow','green','red')
for i in range(100):
    w=random.randint(1,10)
    t.pensize(w)
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    d=random.randint(10,80)
    r=random.randint(0,3)
    t.color(color_list[r])
    draw_square(x,y,d)


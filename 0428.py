import turtle
import random
'''num=int(input('请输入奶牛数量:'))
print(num,'头奶牛七天可以产',num*7*20,'千克牛奶')
num=int(input('请输入一个三位数整数:'))
g=num%10
s=num//10%10
b=num//100
print('个位:',g,'十位:',s,'百位',b)'''
num=int(input('请输入总秒数三位数:'))
g=num%60
s=num//60%60
b=num//3600
print('秒:',g,'分钟:',s,'小时:',b)
num=int(input('请输入长方形的长:'))
num1=int(input('请输入长方形的宽:'))
print((num+num1)*2)
print(num*num1)
n=int(input('请输入乌龟的速度(<10):'))

print()
turtle.pencolor('red')
turtle.pensize(2)
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.forward(200)
turtle.goto(0,-200)
turtle.pencolor('black')
turtle.pensize(2)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)







































































































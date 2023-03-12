import turtle
import random
'''for i in range(5):
    for j in range(5):
        print(i,j)'''
        
'''for i in range(5):
    for j in range(5):
        print(i,end='  ')
    print('\n')'''    


'''for i in range(5):
    for j in range(5):
        print('*',end='')
    print('\n')'''

'''for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print('\n')'''

#乘法口诀
'''for i in range(9):
    for j in range(i+1):
        print(j+1,'*',i+1,'=',(j+1)*(i+1),end=' ')
    print('\n')'''

#乘法口诀
'''for i in range(1,10):
    for j in range(l,i+1):
        print(j,'*',i,'=',i*j,end=' ')
    print('\n')'''



#绘制多边形
'''import turtle as t
import random
s=0
t.speed(30)
t.colormode(255)
t.pensize(3)

for i in range(6):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.color(r,g,b)

    t.circle(60)
    #画多边形
    #for j in range(3):
    #    t.forward(150)
    #    t.right(120) 

    s=60
    t.right(s)'''

#绘制圆圈
import turtle as t
import random
s=0
t.speed(30)
t.colormode(255)
t.pensize(3)

y=0
turtle.color('red')

for i in range(1, 6):
    t.penup()
    t.goto(0, y);
    t.pendown()
    y=y-50
    
    for j in range(i):    
        t.circle(20)
        t.penup()
        t.forward(50)
        t.pendown()
#隐藏箭头   
turtle.ht() 
    

    
























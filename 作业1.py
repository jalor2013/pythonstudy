import random
#SyntaxError:语法错误
#TypeError:类型错误
#NameError:名称错误
#ZeroDivisionError:分母为0报错
#ValueError:值异常错误
#AttributeError:函数属性错误
#IndexError:下标越界异常
#try...except:用来检查异常和处理异常的语句
'''while True:
    try:
        num1=int(input('请输入第1个数:'))
        num2=int(input('请输入第2个数:'))
    except:#except负责在出现报错的时候将报错拦截/捕获
        print('输入错误')
        continue#从这里结束,重新循环
    if num1>num2:
        print(num1,'大')
    elif num1<num2:
        print(num2,'大')
    else:
        print('一样大')'''
print('[比大小游戏]')
while True:
    try:
        num1=int(input('请输入1——100之间的数:'))
    except:
        print('输入错误')
        continue
    num2=random.randint(num1-50,num1+50)
    if 1<=num1<=100:
        if num1>num2:
            print('胜利')
        elif num1<num2:
            print('失败')
        else:
            print('平局')
    else:
        print('数字超出范围')
        
    


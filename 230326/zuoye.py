import random
def choujiang(x,y,z):
    #生成随机数
    w=random.randint(1,4)
    #条件判断
    if w==1:
        print('恭喜'+x+'中奖!')
    elif w==2:
        print('恭喜'+y+'中奖!')
    else:
        print('恭喜'+z+'中奖!')

def choujiang2(x,y,z):
    #定义列表
    list = (x,y,z)
    #生成随机数
    w=random.randint(0,3)
    #打印结果
    print('恭喜'+list[w]+'中奖!')
    
#函数调用        
choujiang2('爸爸','妈妈','孩子')
    

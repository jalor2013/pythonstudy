def jiucuo(text):
    while 1:
        try:
            num=int(input(text))
            return num
            break
        except:
            print('你输错了!!!')
            continue

def chaxun(stu_list,sid):
    result=-1
    i=0
    for temp in stu_list:
        if temp['学号']==sid:
            result=i
            break
        else:
            i=i+1
    return result

############################

print('[学生成绩单系统]')
print('[1]录取成绩单')
print('[2]查询成绩单')
print('[3]显示成绩单')
print('[4]退出系统')

stu_list=[]
while 1:
    num=jiucuo('请输入序号:')
    if num==1:
        score={}
        name=input('请输入姓名:')
        score['姓名']=name
        while 1:
            sid=input('请输入学号:')
            a=chaxun(stu_list,sid)
            if a==-1:
                score['学号']=sid
                break
            else:
                print('-----------------------学号已存在请重新输入----------------------')
                continue
        score['语文']=jiucuo('请输入语文成绩:')
        score['数学']=jiucuo('请输入数学成绩:')
        score['英语']=jiucuo('请输入英语成绩:')
        stu_list.append(score)
        print('--------------------成绩单录取成功-------------------')
    elif num==2:
        print('--------------------正在查询成绩单-------------------')
        sid=input('请输入学号:')
        a=chaxun(stu_list,sid)
        if a==-1:
            print('--------------------所查询学号不存在--------------------')
        else:
            print(stu_list[a])
    



















































































































































































































































        
































































































































































































































































        






























































































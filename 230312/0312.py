txl={'小明':13894623439,'小刚':18946745797,'小红':17837819327}
'''print(txl)
print(txl['小刚'])
print(txl['小红'])
txl['小张']=13526795732
print(txl)
del txl['小明']
print(txl)'''
print('[---通讯录---]')
print('[1]查询联系人')
print('[2]新建联系人')
print('[3]删除联系人')
print('[4]修改联系人')
print('[5]退出通讯录')
while True:
    num=int(input('[请输入服务编号]:'))
    if num==1:
        #查询
        name=input('请输入查询姓名:')
        if name in txl:
            print('---查讯成功---')
            print(name,txl[name])
        else:
            print('---联系人不存在---')
    elif num==2:
        #新建
        name=input('请输入新建姓名:')
        txl[name]=input('请输入新建号码:')
        print('---新建成功---')
    elif num==3:
        #删除
        name=input('请输入要删除的联系人:')
        del txl[name]
        print('---删除成功---')
    elif num==4:
        #修改
        name=input('请输入姓名:')
        if name in txl:
            txl[name]=input('请输入新号码:')
            print('---修改成功---')
            print(name,txl[name])
        else:
            print('---联系人不存在---')
        
    elif num==5:
        print('---退出成功---')
        break

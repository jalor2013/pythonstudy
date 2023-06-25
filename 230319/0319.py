account={'abc123':'12345'}
print('---用户登录系统---')
print('[1]---登录账号---')
print('[2]---注册账号---')
print('[3]---修改密码---')
while True:
    num=int(input('[请输入您选择的服务序号]:'))
    if num==1:
        print('[---您正在登录账号---]')
        user=input('请输入用户名:')
        code=input('请输入密码:')
        if user in account:
            if code==account[user]:
                print('登录成功')
            else:
                print('[密码错误,登录失败]')
        else:
            print('[用户名不存在]')
    elif num==2:
        print('[---您正在创建账号---]')
        user=input('请输入用户名:')
        code=input('请输入密码:')
        if user in account:
            print('[用户名已存在!]')
        else:
            print('用户名可以使用')
            account[user]=code
            print('[账号创建成功]')
     
        
        
        
                
        

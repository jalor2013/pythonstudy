import sys

#图书管理系统:图书类:创建书的实例对象   图书管理类:创建出图书管理员对象

#【1】图书类:书名,作者,状态,序号
class book():
    def __init__(self,name,author,num):
        self.name=name
        self.author=author
        self.state='未借出'
        self.num=num
        
    def __str__(self):
        return f'书名{self.name}/n作者:{self.author}/n状态:{self.state}/n序号:{self.num}'

class book_manager():#图书管理类的创建:添加书,查询书,借书,还书
    def __init__(self):
        self.book_list=[]
        
    def add_book(self):
        name=input('书名:')
        author = input('作者:')
        num = input('序号:')
        self.book_list.append( book(name, author,num) )
        
        print(f'《{name}》添加成功')
        
    def find_book(self,name):
        find = False
        for i in self.book_list:
            if i.name==name:
                find = True
                print(i)
            
        if find != True:
            print('没有这本书')


    def borrow_books(self,name):#借书
        find = False
        for i in self.book_list:
            if i.name==name and i.state == '未借出':
                find = True
                i.state = '已借出'
                print(i)
                return
            
        if find != True:
            print('没有这本书')
            
    def returning_book(self,name):
        for i in self.book_list:
            if i.name==name and i.state == '已借出':
                i.state = '未借出'
                print(i)
                return
            
        
                
manager=book_manager()
print('[图书管理系统]')
print('[1]添加图书[2]查询图书[3]借书[4]还书[5]退出')
        
while 1:
    num=input('请输入服务序号:')
    if num=='1':
        print('------正在添加图书------')
        manager.add_book()
    elif num=='2':
        print('------正在查询图书------')
        manager.find_book(input('请输入要找的书:'))
        
    elif num=='3':
        print('------正在借书------')
        manager.borrow_books(input('请输入要借的书:'))
    elif num=='4':
        print('------正在还书------')
        manager. returning_book(input('请输入要还的书名:'))
    elif num=='5':
        print('------系统已退出------')
        sys.exit(0);
    else:
        print('请输入正确的服务序号')


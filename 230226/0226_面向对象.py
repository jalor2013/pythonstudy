#面向过程：将一个项目的每一步逐步的去实现
#面向对象：
#洗衣服：洗衣机洗，手洗
#手洗：放水，放衣服，加洗衣液，拧干，漂洗，晾晒（面向过程）
#洗衣机：放衣服，按按钮，（面向对象）洗衣机就是实现洗衣服功能的
#class类 创建类的方法：class类名（）：
#面向对象基础知识点
#1.理解面向对象
#面向对象就是将编程当成一个事物，对外界来说，事物是直接使用的，不用管他内部的情况
#而编程就是设置事物能够做什么事情
#2.类和对象
#类和对象的关系：同类去创建一个对象
#类是对一系列
'''class washer():
    def wash(self):
        print('开始洗衣服')
    def dry(self):
        print('开始脱水')
    
    
    
haier=washer()
haier.wash()
haier.dry()'''
class car():
    def zhizou(self):
        print('往前走')
    def guaiwan(self):
        print('拐弯')
    def tingxia(self):
        print('停车')
    def wanghouzou(self):
        print('往后走')
    def zidongjiashi(self):
        print('自动驾驶')
fengtian=car()
fengtian.zhizou()
fengtian.guaiwan()        
fengtian.tingxia()
fengtian.wanghouzou()
fengtian.zidongjiashi()

import random
import os

print('            *')
print('          *   *')
print('         *     *')
print('        *    *  *')
print('       *   *  *  *')
print('      *   *    *  *')
print('     *   *      *  *')
print('    *   *    *      *')
print('   *   *         *   *')
print('  *   *           *   *')
print(' *   *             *   *')
print('             *        ')
print('             *')
print('             *')

os.system("clear")

age = random.randint(1,20)
print('小朋友，你知道我几岁吗？来猜一猜吧！')
while True:
    a = int(input("\n输入岁数， enter确认\n"))
    if(a > age):
      print('猜大了，再试试')
    elif (a < age):
        print('猜小了，再试试')
    else:
        print("你猜对了，你好棒！")
        break;
    


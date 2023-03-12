'''a=0
while a<10:
    print(a)
  a=a+1'''
right_answer='ACBACCAADC'
print('请输入您的10个答案,用大写的字母')

while True:
    answer=input('请输入答案:')
    if len(right_answer)==len(answer):
        print('答案数量正确')
        break
    else:
        print('答案数量错误')
        
score=0
results=''

for i in range(10):
    if right_answer[i]==answer[i]:
        score=score+10
        results=results+answer[i]
    else:
        results=results+'X'
print('正确答案:'+right_answer)
print('你的答案:'+answer)
print('改卷结果:'+results)
print('得分：',score)

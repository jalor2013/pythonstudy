def yzsxh(num):
    g=num%10
    s=num//10%10
    b=num//100
    if g*g*g+s*s*s+b*b*b==num:
        print(num,'是水仙花数')
    else:
        pass

for i in range(100,1000):
    yzsxh(i)

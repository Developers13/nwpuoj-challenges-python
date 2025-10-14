from math import sqrt as sq
# 功能：判断输入的两条边能否与第三边组成直角三角形，并输出是哪条边为斜边或不能组成

a=int(input())
b=int(input())
ls=[a,b]
ls.sort()
def func(l):
    if(sq(l[0]**2+l[1]**2)%1==0):
        return 'c'
    elif((t:=sq(l[1]**2-l[0]**2))%1==0):
        if(t<l[0]):
            return 'a'
        else:
            return 'b'
    else:
        return 'non'
print(func(ls))

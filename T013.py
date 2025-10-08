from math import sqrt as sq
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
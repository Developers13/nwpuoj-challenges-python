import math
def exgcd(a,b):
    if b==0:
        return 1,0,a
    else:
        x,y,q=exgcd(b,a%b)
        x,y=y,x-(a//b)*y
        return x,y,q
a,b=map(int,input().split())
x,y,q=exgcd(a,b)
print(x,y)
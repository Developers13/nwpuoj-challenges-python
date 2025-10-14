# 功能：解二元一次方程组并判断特殊情况
from math import gcd
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if(a/d == b/e != c/f):
    print("error")
else:
    cd1 = gcd(a, d)
    #eliminate x
    t1 = cd1 / a
    t2 = cd1 / d
    a1 = cd1
    d1 = cd1
    b1 = b * t1
    c1 = c * t1
    e1 = e * t2
    f1 = f * t2
# ...原始代码后续...
from math import *
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
    e1 = e1 - b1
    f1 = f1 - c1
    y = f1 / e1
    x = (c - b * y) / a
    print(f"{x:.3f} {y:.3f}")
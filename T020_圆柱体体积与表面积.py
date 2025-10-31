import math
h=float(input())
r=float(input())
PI=math.acos(-1.0)
V=PI*r*r*h
S=PI*r*r*2+2*PI*r*h
print("%.4f"%V)
print("%.4f"%S)


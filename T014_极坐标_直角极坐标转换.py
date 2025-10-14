from math import hypot, atan
# 功能：将直角坐标(x, y)转换为极坐标(r, θ)

x=int(input())
y=int(input())
print(f"{hypot(x,y):.4f},{atan(y/x):.4f}")

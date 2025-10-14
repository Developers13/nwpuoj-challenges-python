# 功能：递归计算吃糖果的方法数（每次可吃1或2颗）
ql = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        ql.append(x)
def eatCandy(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return eatCandy(n-1) + eatCandy(n-2)
for i in range(len(ql)):
    print(eatCandy(ql[i]))

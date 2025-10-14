# 功能：计算n!（n的阶乘）末尾连续零的个数
n = int(input())
fac = 1
for i in range(1, n+1):
    fac *= i
sum = 0
for j in reversed(str(fac)):
    if j == '0':
        sum += 1
    else:
        break
print(sum)

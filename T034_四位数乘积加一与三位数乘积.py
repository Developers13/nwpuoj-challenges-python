# 功能：找出满足条件的四位数和三位数乘积
q = int(input())
for d in range(10,100):
    if 1000<=q * d + 1 < 10000 and (100 <= (q%10) * d < 1000):
        print((q * d) + 1, d)

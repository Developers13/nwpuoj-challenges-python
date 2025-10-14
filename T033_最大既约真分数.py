# 功能：求不大于a/b且分母不超过n的最大既约真分数
from math import gcd, floor
n, a, b = (map(lambda x: int(x), input().split()))
best_x, best_y = 0, 1
for y in range(1, n + 1):
    x = (a*y - 1) // b
    if x>=1 and gcd(x, y) == 1:
        if x * best_y > best_x * y:
            best_x, best_y = x, y
print(f"{best_x}/{best_y}")

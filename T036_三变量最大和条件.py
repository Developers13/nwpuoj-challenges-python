# 功能：三变量满足特定条件下的最大和
n = int(input())
max_sum = 0
for a1 in range(n+1):
    for a2 in range(n+1):
        for a3 in range(n+1):
            if (a1 + a2) % 2 == 0 and (a2 + a3) % 3 == 0 and (a1 + a2 + a3) % 5 == 0:
                if a1 + a2 + a3 > max_sum:
                    max_sum = a1 + a2 + a3
print(max_sum)

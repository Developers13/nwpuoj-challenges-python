# 功能：将数字n重复拼接m次后累加求和
n = input()
m = int(input())
sum = 0
for i in range(1,m+1):
    sum += int(n*i)
print(sum)

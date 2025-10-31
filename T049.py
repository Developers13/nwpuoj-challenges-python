n = int(input())
res = 1
for i in range(2,n+1):
    res *= (n+i)/i
print(int(res))
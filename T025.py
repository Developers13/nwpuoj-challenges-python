n = int(input())
oper = 0
while int(n) > 0:
    m = 0
    for i in range(len(str(n))):
        m += int(str(n)[i])
    n -= m
    oper += 1
print(oper)
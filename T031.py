ql =[]
while True:
    n = int(input())
    if n == 0:
        break
    ql.append(int(n))

def upStair(stair) -> int:
    if stair == 0:
        return 1
    elif stair < 0:
        return 0
    else:
        return upStair(stair-1) + upStair(stair-2) + upStair(stair-3)
for i in range(len(ql)):
    print(upStair(ql[i]))
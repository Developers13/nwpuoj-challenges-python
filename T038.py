ql = []
while True:
    s = list(map(int, list(input().split(','))))

    if any(i < 0 for i in s):
        break
    else:
        ql.append(s)
#p1002过河卒问题
def dp(bi, bj, pi, pj):
    a =[[1 for _ in range(bj+1)] for _ in range(bi+1)]
    if 0 <= pi <= bi and 0 <= pj <= bj:
        a[pi][pj] = 0
    for x in range(bi+1):
        for y in range(bj+1):
            if x == 0 or y == 0:
                continue
            elif x == pi and y == pj:
                continue
            else:
                a[x][y] = a[x-1][y] + a[x][y-1]
    return a[bi][bj]
for i in range(len(ql)):
    print(dp(ql[i][0], ql[i][1], ql[i][2], ql[i][3]))



            
    
        
#p1244青蛙过河
#当没有石墩时，设有Y个荷叶，则最多Y+1只过河
#有S个石墩时，f(s,y) = 2*f(s-1,y)，可以把一个石墩看作中转
ql=[]
while True:
    s,y = map(int, input().split(","))
    if s<0 or y<0:
        break
    else:
        ql.append((s,y))
for i in range(len(ql)):
    print(pow(2,ql[i][0])*(ql[i][1]+1))

n=int(input())
sum=0
if(n<0 or n>36):
    print(0)
for a in range(10):
    for b in range(10):
        for c in range(10):
            d=n-a-b-c
            if(0<=d<10):
                sum+=1
print(sum)
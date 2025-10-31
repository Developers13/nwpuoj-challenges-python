def Defactor(n,m):
    if(n==1):
        return 1
    if(m==1):
        return 0
    ans=Defactor(n,m-1)
    if(n%m==0):
        ans+=Defactor(n//m,m)
    return ans
       
a=int(input())
print(Defactor(a,a))


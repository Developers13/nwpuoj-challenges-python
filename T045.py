def Divide(m,n):
    if m==0 or n==1:
        return 1
    if(m<n):
        return Divide(m,m)
    return Divide(m-n,n)+Divide(m,n-1)
m,n=map(int,input().split())
print(Divide(m,n))
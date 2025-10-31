def Collatz_conjecture(n):
    a.append(n)
    if(n==1):
        return
    if(n%2):
        n=n*3+1
        Collatz_conjecture(n)
    else:
        n//=2
        Collatz_conjecture(n)
a=[]
n=int(input())
Collatz_conjecture(n)
a=map(str,a)
print(','.join(a))

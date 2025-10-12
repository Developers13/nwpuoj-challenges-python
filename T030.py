fib = [0,1,1]
n = int(input())
for i in range(3,n+1):
    fib.append(fib[i-1]+fib[i-2])
print(fib[n])

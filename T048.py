def dfs(t,w,v):
    if(t==n+1):
        return (w==v)
    ans=0
    for i in range(0,v-w+1):
        ans+=dfs(t+1,w+i,v)
    return ans
    pass

n,v=map(int,input().split())
print(dfs(1,0,v))
#dfs
def dfs(x,y,x2,y2) -> bool:
    if x==x2 and y==y2:
        return True
    if x>x2 or y>y2:
        return False
    return dfs(x+y,y,x2,y2)|dfs(x,y+x,x2,y2)
x1,y1,x2,y2 = map(int,input().split())
if dfs(x1,y1,x2,y2):
    print("true")
else:
    print("false")
ql = []
while True:
    s = input()
    if s == '0':
        break
    else:
        ql.append(int(s))
def flooring(n):
    f = [0]
    for i in range(1,n+1):
        if i % 2 != 0:
            f.append(0)
        else:
            if i == 2:
                f.append(3)
            elif i == 4:
                f.append(11)
            else:
                #n = 2m
                #f(n) = 3f(n-1) + 2(f(n-2) + f(n-3) + ... + f(2) + f(1))
                f.append(4*f[i-2]-f[i-4])
    return f
maxn = max(ql)
f = flooring(maxn)
for i in range(len(ql)):
    print(f[ql[i]] % 100003)
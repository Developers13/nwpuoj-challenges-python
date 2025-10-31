def Hofstader_F(n):
    if n == 0:
        return 1
    else:
        return n - Hofstader_M(Hofstader_F(n - 1))
def Hofstader_M(n):
    if n == 0:
        return 0
    else:
        return n - Hofstader_F(Hofstader_M(n - 1))
n = int(input())
print(Hofstader_F(n), Hofstader_M(n),sep=' ')

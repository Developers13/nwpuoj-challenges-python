# 功能：判断输入的数字是否为回文数
n = input()
for i in range(len(n)//2):
    if (n[i] != n[-i-1]):
        print("No")
        exit()
        break
    else:
        continue
print("Yes")

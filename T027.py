n = input()
for i in range(len(n)//2):
    if (n[i] != n[-i-1]):
        print("No")
        exit()
        break
    else:
        continue
print("Yes")
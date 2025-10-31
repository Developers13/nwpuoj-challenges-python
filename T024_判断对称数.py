# 功能：判断输入的数字是否为对称数（回文数或镜像数）
def core(n: str, m: str)-> bool:
    match (n, m):
        case ('0', '0') | ('1', '1') | ('6', '9') | ('8', '8') | ('9', '6'):
            return True
        case _:
            return False

def determineSymmetricNumber(num: str):
    if int(num) < 0:
        print("No")
        return
    # 奇数长度需要中间字符是 0/1/8
    if (len(num) % 2) != 0:
        mid = num[len(num)//2]
        if mid not in ('0', '1', '8'):
            print("No")
            return
    # 检查对称对
    for i in range(len(num)//2):
        if core(num[i], num[-i-1]):
            continue
        else:
            print("No")
            return
    print("Yes")

determineSymmetricNumber(input())
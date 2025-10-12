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
    if (len(num) % 2) != 0:
        if(num[len(num)//2 + 1] == '0' or '1' or '8'):
            for i in range(len(num)//2):
                if(core(num[i], num[-i-1])):
                    continue
                else:
                    print("No")
                    return
            print("Yes")
            return
        else:
            print("No")
            return
    else:
        for i in range(len(num)//2):
            if(core(num[i], num[-i-1])):
                continue
            else:
                print("No")
                return
        print("Yes")
        return
n = input()
determineSymmetricNumber(n)
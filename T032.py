ql = []
while True:
    s = input()
    if s.split()[0] <= '0' or s.split()[1] <= '0':
        break
    else:
        ql.append((s.split()[0], s.split()[1]))
def powSingle(a: str, b: int) -> int:
    if a == '1':
        return 1
    elif a =='2':
        match b % 4:
            case 1:
                return 2
            case 2:
                return 4
            case 3:
                return 8
            case 0:
                return 6
    elif a == '3':
        match b % 4:
            case 1:
                return 3
            case 2:
                return 9
            case 3:
                return 7
            case 0:
                return 1
    elif a == '4':
        match b % 2:
            case 1:
                return 4
            case 0:
                return 6
    elif a == '5':
        return 5
    elif a == '6':
        return 6
    elif a == '7':
        match b % 4:
            case 1:
                return 7
            case 2:
                return 9
            case 3:
                return 3
            case 0:
                return 1
    elif a == '8':
        match b % 4:
            case 1:
                return 8
            case 2:
                return 4
            case 3:
                return 2
            case 0:
                return 6
    elif a == '9':
        match b % 2:
            case 1:
                return 9
            case 0:
                return 1
for i in range(len(ql)):
    print(powSingle(ql[i][0][-1], int(ql[i][1])))

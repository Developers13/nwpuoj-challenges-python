# 功能：计算大数幂的末位数字规律
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
# ...原始代码后续...
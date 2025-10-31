# 功能：计算大数幂的末位数字规律
cycles = {
    '0': [0],
    '1': [1],
    '2': [2,4,8,6],
    '3': [3,9,7,1],
    '4': [4,6],
    '5': [5],
    '6': [6],
    '7': [7,9,3,1],
    '8': [8,4,2,6],
    '9': [9,1],
}

def powSingle(last_digit: str, b: int) -> int:
    # 约定：调用前已处理 b==0 的特殊情况（若需要可在这里也处理）
    if b == 0:
        return 1
    cycle = cycles.get(last_digit, [0])
    # cycle 长度为1 的直接返回
    if len(cycle) == 1:
        return cycle[0]
    idx = (b - 1) % len(cycle)
    return cycle[idx]

pairs = []
while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    parts = line.split()
    if len(parts) < 2:
        continue
    a_str, b_str = parts[0], parts[1]
    try:
        b = int(b_str)
    except ValueError:
        continue
    # 常见终止条件：当且仅当 a==0 且 b==0 时结束（根据题目要求可调整）
    if a_str == '0' and b == 0:
        break
    last = a_str[-1]
    pairs.append((last, b))

for last, b in pairs:
    # 若 b==0 且 last=='0' 上面已把 (0,0) 当作结束；0^0 通常作为结束信号处理
    # 对于 b==0 的一般情况，返回 1
    if b == 0:
        print(1)
    else:
        print(powSingle(last, b))
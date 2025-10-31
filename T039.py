n = int(input())
def stickNumber(n):
    l = (6,2,5,5,4,5,6,3,7,6)
    sum = 0
    for A in range(10):
        for B in range(10):
            C = A + B
            if 0 <= C < 10 and n == l[A] + l[B] + l[C] + 4:
                sum += 1
    return sum
print(stickNumber(n))           
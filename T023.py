def testParallel(a, b, c, d):
    vector1 = (b[0] - a[0], b[1] - a[1])
    vector2 = (d[0] - c[0], d[1] - c[1])
    if(vector1[0] * vector2[1] == vector1[1] * vector2[0]):
        print("Yes")
    else:
        print("No")
x1 =int(input())
y1 =int(input())
x2 =int(input())
y2 =int(input())
x3 =int(input())
y3 =int(input())
x4 =int(input())
y4 =int(input())
testParallel((x1, y1), (x2, y2), (x3, y3), (x4, y4))
    
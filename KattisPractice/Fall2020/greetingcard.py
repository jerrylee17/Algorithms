import math
pp = int(input())
targetNum = int(math.sqrt(2018**2 // 2))
currPoints = set([])
cases = [(0, 2018), (1118, 1680)]


def generateCases(point):
    x, y = point
    res = []
    for c in cases:
        p1 = (x + c[0], y - c[1])
        p2 = (x + c[0], y + c[1])
        p3 = (x - c[0], y - c[1])
        p4 = (x - c[0], y + c[1])
        p5 = (x + c[1], y - c[0])
        p6 = (x + c[1], y + c[0])
        p7 = (x - c[1], y - c[0])
        p8 = (x - c[1], y + c[0])
        res.extend([p1, p2, p3, p4, p5, p6, p7, p8])
    for c in res:
        if c[0] < 0 or c[1] < 0:
            res.remove(c)
    res = list(set(res))
    return res


def checkCases(point, currPoints):
    pointsToCheck = generateCases(point)
    subtotal = 0
    for p in pointsToCheck:
        if p in currPoints:
            subtotal += 1
    return subtotal


count = 0
for _ in range(pp):
    a, b = list(map(int, input().split(' ')))
    currPoints.add((a, b))
    count += checkCases((a, b), currPoints)
print(count)

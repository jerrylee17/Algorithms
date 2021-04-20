import math
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

def calcDist(a, b):
    return math.sqrt((b[0] - a[0])**2+(b[1] - a[1])**2)

def midPoint(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

def nextPoint(p, m):
    dx = m[0] - p[0]
    dy = m[1] - p[1]
    return (m[0] + dx, m[1] + dy)

p12 = calcDist(p1, p2)
p13 = calcDist(p1, p3)
p23 = calcDist(p2, p3)

if p12 == p13:
    # 2, 1, 3
    m = midPoint(p2, p3)
    res = nextPoint(p1, m)
    print(int(res[0]), int(res[1]))
    # dy = p1[1] - p2[1]
    # dx = p1[0] - p2[0]
    # lastPoint = (p3[0] - dx, p3[1] - dy)
    
elif p12 == p23:
    # 1, 2, 3
    m = midPoint(p1, p3)
    res = nextPoint(p2, m)
    print(int(res[0]), int(res[1]))
    # dy = p2[1] - p1[1]
    # dx = p2[0] - p1[0]
    # lastPoint = (p3[0] - dx, p3[1] - dy)
elif p13 == p23:
    # 1, 3, 2
    m = midPoint(p1, p2)
    res = nextPoint(p3, m)
    print(int(res[0]), int(res[1]))
    # dy = p3[1] - p1[1]
    # dx = p3[0] - p1[0]
    # lastPoint = (p2[0] - dx, p2[1] - dy)




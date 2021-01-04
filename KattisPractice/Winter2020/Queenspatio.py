import math
tc = int(input())


def calcRadius(n, m):
    # Calculate first radius jump from 1 to m
    """
    angle = 360/n
    sides = 2r1, 1 + r1, 1 + r1
    law of cosines....
    a^2 = b^2+b^2-2b^2cosa = (2b^2)(1-cosa)
    (4r1**2) = (2(1+r1)**2) * (1-cos(angle))
    2r1**2 = (1+r1)**2 * (1-cos(angle))
    """
    # Every jump after the first is just a 45-45-90 triangle
    for i in range(m-1):
        pass
    return 4


def calcFence(radius, n):
    result = 2*n*radius + (2*radius*math.pi)
    return result


for _ in range(tc):
    k, n, m = list(map(int, input().split(' ')))
    radius = calcRadius(n, m)
    fence = calcFence(radius, n)
    print(f'{k} {round(radius, 3)} {round(fence, 3)}')

import math
sin = math.sin
cos = math.cos
pi = math.pi
g = 9.81
tc = int(input())


def calcT(x, v, theta):
    rtheta = theta * pi / 180
    return (x / (v*cos(rtheta)))


def calcY(v, t, theta):
    rtheta = rtheta = theta * pi / 180
    return (v*t*sin(rtheta) - 0.5*g*t**2)


for _ in range(tc):
    v, theta, x, h1, h2 = list(map(float, input().split(' ')))
    t = calcT(x, v, theta)
    height = calcY(v, t, theta)
    if (h1 + 1) < height < (h2 - 1):
        print("Safe")
    else:
        print("Not Safe")

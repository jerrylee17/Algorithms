import sys
n = int(input())

points = []
for i in range(n):
    x, y = list(map(float, input().split(' ')))
    points.append([x, y])

points.sort(key=lambda x: x[0])
lip = 0
for (x1, y1), (x2, y2) in zip(points[:-1], points[1:]):
    if lip == 0:
        lip = abs(y1-y2)/abs(x1-x2)
    else:
        lip = max(lip, abs(y1-y2)/abs(x1-x2))
print(lip)

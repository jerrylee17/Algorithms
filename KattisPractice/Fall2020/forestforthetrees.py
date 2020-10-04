import math
x, y = list(map(int, input().split(' ')))
x1, y1, x2, y2 = list(map(int, input().split(' ')))

xygcd = math.gcd(x, y)
xjump = x / xygcd
yjump = y / xygcd
# Generate lattice points
for i in range(1, xygcd):
    x, y = (xjump*i, yjump*i)
    if x1 <= x <= x2 and y1 <= y <= y2:
        continue
    else:
        print("No")
        print(int(x), int(y))
        break
else:
    print("Yes")

import math
h, v = list(map(int, input().split()))

# how the hell do you do this

xd = math.sin(v*math.pi/180)
res = math.ceil(h / xd)
print(res)

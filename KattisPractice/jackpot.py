import math
machines = int(input())

for i in range(machines):
    wheels = int(input())
    arr = input()
    arr = arr.split(' ')
    arr = [int(a) for a in arr]
    res = 1
    for x in arr:
        res = res*x/math.gcd(res, x)
        res = int(res)
        if res > 1_000_000_000:
            break
    if res <= 1_000_000_000:
        print(res)
    else:
        print("More than a billion")

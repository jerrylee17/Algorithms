import math
tc = int(input())


def distanceInRange(a, b, target):
    return (
        math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2) <= target
    )


def findLocation(hatchets, size):
    for i in range(size):
        for j in range(size):
            max_length = min([
                i,
                size - i,
                j,
                size - j
            ])
            p1 = (i, j)
            for h in hatchets:
                if p1 == h:
                    break
                if not distanceInRange(p1, h, max_length):
                    break
            else:
                print(i, j)
                return
    print('poodle')
    return


for _ in range(tc):
    s, h = list(map(int, input().split(' ')))
    hatches = []
    for i in range(h):
        x, y = list(map(int, input().split(' ')))
        hatches.append((x, y))
    findLocation(hatches, s)

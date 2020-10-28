import sys


def randNumGen(r):
    return (r*5_171+13_297) % 50_021


def forestFires(r, n):
    i = 0
    r = randNumGen(r)
    m = r
    treeCoords = {}
    count = 0
    while i < n:
        m = randNumGen(m)
        for _ in range(10000):
            x, y = 0 if not str(m)[-4:-2] else (
                int(str(m)[-4:-2])
            ), 0 if not str(m)[-2:] else int(str(m)[-2:])
            if (x, y) in treeCoords.values():
                m = randNumGen(m)
                continue
            else:
                treeCoords[i] = (x, y)
                break
        else:
            print("didnt break")
        m = randNumGen(m)
        a = treeCoords[m % (i+1)]
        m = randNumGen(m)
        b = treeCoords[m % (i+1)]
        if (
            abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 0
            or abs(a[0] - b[0]) == 0 and abs(a[1] - b[1]) == 1
        ):
            count += 1
        i += 1
        if i % 100 == 0:
            print(count, end=' ')
            count = 0
    print(treeCoords)


for line in sys.stdin:
    if not line.strip():
        break
    r, n = list(map(int, line.split(' ')))
    forestFires(r, n)
    print()

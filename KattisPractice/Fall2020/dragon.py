while True:
    n, m = list(map(int, input().split(' ')))
    if n == 0 and m == 0:
        break
    dragonHead = []
    for i in range(n):
        dragonHead.append(int(input()))
    knights = []
    for j in range(m):
        knights.append(int(input()))
    dragonHead.sort()
    knights.sort()
    total = 0
    i, j = 0, 0
    while True:
        if knights[i] >= dragonHead[j]:
            total += knights[i]
            i += 1
            j += 1
        else:
            i += 1
        if j == len(dragonHead):
            print(total)
            break
        if i == len(knights):
            print('Loowater is doomed!')
            break

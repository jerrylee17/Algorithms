c, n = list(map(int, input().split()))

train = []
for i in range(n):
    train.append(list(map(int, input().split())))

p = 0
for t in train:
    if t[0] > p:
        print('impossible')
        break
    p += t[1] - t[0]
    if p < 0 or p > c:
        print('impossible')
        break
    if t[2] > 0 and p != c:
        print('impossible')
        break
else:
    if p != 0:
        print('impossible')
    else:
        print('possible')

tc = int(input())

times = []
for _ in range(tc):
    x, y = list(map(int, input().split(' ')))
    times.append((x, y))

s = set([])
for x, y in times:
    for p in range(x, y+1):
        s.add(p)
print(len(s))


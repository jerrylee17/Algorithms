n, m, s, t = list(map(int, input().split(' ')))
links = []
squawks = [0 for i in range(n)]


for _ in range(m):
    x, y = list(map(int, input().split(' ')))
    connection = (x, y)
    links.append(connection)
    # Duplicating so its symmetrical
    connection = (y, x)
    links.append(connection)


links.sort(key=lambda x: (x[0], x[1]))


def updateSquawks(squawks, links):
    newSq = [0 for i in range(len(squawks))]
    for l in links:
        host, target = l
        newSq[target] += squawks[host]
    return newSq


squawks[s] = 1
for i in range(t):
    squawks = updateSquawks(squawks, links)

if t == 0:
    print(0)
else:
    print(sum(squawks))

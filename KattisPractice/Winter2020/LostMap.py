v = int(input())

roads = []
for i in range(v):
    road = list(map(int, input().split(' ')))
    roads.append(road)


def getPoints(r):
    minimum, index = 10**7, 0
    for j, m in enumerate(r):
        if m != 0 and m < minimum:
            minimum = m
            index = j
    return index


sol = set([])
for i, r in enumerate([x.copy() for x in roads]):
    while True:
        index = getPoints(r)
        s = min(i+1, index+1), max(i+1, index+1), r[index]
        if s in sol:
            r[index] = 0
        else:
            break
    sol.add(s)
sol = list(sol)
graph = {}
for r in sol:
    graph[r[0]] = graph.get(r[0], []) + [r[1]]
    graph[r[1]] = graph.get(r[1], []) + [r[0]]


sol.sort(key=lambda x: (x[0], x[1]))
for s in sol:
    print(s[0], s[1])

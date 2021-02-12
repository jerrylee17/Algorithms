from collections import deque
from math import sqrt

a, f = list(map(int, input().split(' ')))
l, w = list(map(int, input().split(' ')))

def checkElsaJump(jump, s1, s2):
    distance = sqrt((s1[0]-s2[0])**2+(s1[1]-s2[1])**2)
    return distance <= jump

def ElsaGoal(safe, a, s, g):
    safes = safe.copy()
    queue = deque()
    queue.append([s, 0])
    while len(queue):
        pos = queue.popleft()
        if pos[0] == g:
            return pos[1]
        for w in safes.copy():
            if checkElsaJump(a, pos[0], w):
                queue.append([w, pos[1] + 1])
                safes.remove(w)
    return -1

def FatherGoal(safe, a, s, g):
    safes = safe.copy()
    queue = deque()
    queue.append([s, 0])
    while len(queue):
        pos = queue.popleft()
        # Search in safe spaces
        if pos[0] == g:
            return pos[1]
        for w in safes.copy():
            if ((abs(pos[0][0] - w[0]) <= a and pos[0][1] == w[1]) or 
            (abs(pos[0][1] - w[1]) <= a and pos[0][0] == w[0])) :
                queue.append([w, pos[1] + 1])
                safes.remove(w)
    return -1

# Make board
s, g = (0,0), (0,0)
safe = []
for i in range(l):
    row = input()
    for j, e in enumerate(row):
        if e == 'W':
            safe.append((i, j))
        # Find start
        if e == 'S':
            s = (i, j)
            safe.append((i, j))
        elif e == 'G':
            safe.append((i, j))
            g = (i, j)

elsa = ElsaGoal(safe, a, s, g)
father = FatherGoal(safe, f, s, g)

if elsa == -1 and father == -1:
    print("NO WAY")
elif elsa == -1:
    print("NO CHANCE")
elif father == -1:
    print("GO FOR IT")
elif elsa > father:
    print("NO CHANCE")
elif father > elsa:
    print("GO FOR IT")
elif elsa == father:
    print("SUCCESS")

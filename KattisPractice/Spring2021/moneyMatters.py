n, m = list(map(int, input().split()))

# class node:
#     def __init__(self, val):
#         self.val = val
#         self.neighbors = set()
#         self.used = False

people = []
for i in range(n):
    people.append([int(input()), False, []])

for i in range(m):
    p1, p2 = list(map(int, input().split()))
    people[p1][2].append(p2)
    people[p2][2].append(p1)
    # people[p1].neighbors.add(p2)
    # people[p2].neighbors.add(p1)

for p in people:
    if p[1]:
        continue
    p[1] = True
    subT = p[0]
    queue = p[2]
    while queue:
        ind = queue.pop(0)
        x = people[ind]
        if x[1]:
            continue
        subT += x[0]
        people[ind][1] = True
        queue.extend(list(x[2]))
        queue = list(set(queue))
    if subT != 0:
        print('IMPOSSIBLE')
        break
else:
    print('POSSIBLE')
        
# loop through people
# for p in people:
#     if p.used:
#         continue
#     p.used = True
#     subT = p.val
#     queue = list(p.neighbors)
#     while queue:
#         x = people[queue.pop(0)]
#         if x.used:
#             continue
#         subT += x.val
#         x.used = True
#         queue.extend(list(x.neighbors))
#     if subT != 0:
#         print('IMPOSSIBLE')
#         break
# else:
#     print('POSSIBLE')

        
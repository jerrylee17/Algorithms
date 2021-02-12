import math
n, m = list(map(int, input().split(' ')))

edges = {}
# Set up edges
for i in range(n):
    edges[i+1] = []

for i in range(m):
    u, v = list(map(int, input().split(' ')))
    edges[u].append(v)
    edges[v].append(u)

# Brute force
# Calculate needed for every edge
# lengths = [0 for i in range(n)]
done = set([])
islands = 0
evenIslands = True
# counter = 0
# Find islands
for i in range(1, n+1):
    if i in done:
        continue
    s = set([i])
    queue = [i]
    # Propogate through node
    while queue:
        node = queue.pop()
        newNodes = set([])
        # Add its neighbors
        newNodes = newNodes | set(edges[node])
        # Filter existing nodes
        newNodes = newNodes & (newNodes ^ s)
        queue.extend(list(newNodes))
        s = s | newNodes
    islands += 1
    if len(s) == 1:
        counter += 1
    done = done | s
# print(islands)

# Find groups
# done = set([])
# for i in range(1, n+1):
#     if i in done:
#         continue
#     s = set([i])
#     queue = [i]
#     # Propogate through node
#     while queue:
#         node = queue.pop()
#         newNodes = set([])
#         # Add its neighbors
#         for edge in edges[node]:
#             newNodes = newNodes | set(edges[edge])
#         newNodes = newNodes & (newNodes ^ s)
#         queue.extend(list(newNodes))
#         s = s | newNodes
#     counter += 1
#     done = done | s

# evenIslands = int(counter == (islands * 2))
total = (islands - 1) + (evenIslands)
print(total)




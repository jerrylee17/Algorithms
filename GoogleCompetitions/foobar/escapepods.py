def solution(entrances, exits, path):
    '''
    FLOW problem
    entrances = source
    exits = sink
    '''
    # Create source/sink nodes
    max_cap = 2_000_000
    for p in path:
        p.extend([0,0])
    source = [0 for i in range(len(path[0]))]
    sink = [0 for i in range(len(path[0]))]
    for x in entrances:
        source[x] = max_cap
    for x in exits:
        path[x][len(path[0]) - 1] = max_cap
    path.append(source)
    path.append(sink)

    # Capacity
    # mat = [[0 for i in range(len(path))] for j in range(len(path))]
    
    def bfs(s, t, arr):
        visited = [False] * len(path)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            n = queue.pop(0)
            for i, v in enumerate(path[n]):
                if not visited[i] and v > 0:
                    if i == t:
                        arr[i] = n
                        return True
                    queue.append(i)
                    visited[i] = True
                    arr[i] = n
        return False
    
    def getFlow(source, sink):
        arr = [-1 for i in range(len(path))]
        max_flow = 0
        while bfs(source, sink, arr):
            pf = float("inf")
            s = sink
            while s != source:
                pf = min(pf, path[arr[s]][s])
                s = arr[s]
            max_flow += pf
            v = sink
            while v != source:
                u = arr[v]
                path[u][v] -= pf
                path[v][u] += pf
                v = arr[v]
        return max_flow
    
    sol = getFlow(len(path)-2, len(path)-1)
    return sol

# p = solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
p = solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])


print(p)


def solution(times, times_limit):

    def BellmanFord(v):
        dist = [float("Inf")] * len(times)
        dist[v] = 0
        
        for _ in range(len(times) - 1):
            updated = False
            for i in range(len(times)):
                for j in range(len(times)):
                    # dist[j] = min(dist[i] + times[i][j], dist[j])
                    if dist[i] != float('inf') and dist[i] + times[i][j] < dist[j]:
                        dist[j] = dist[i] + times[i][j]
                        updated = True
            if not updated:
                break

        # Negative cycle detection
        for i in range(len(times)):
            for j in range(len(times)):
                # if dist[i] + times[i][j] < dist[j]:
                if dist[i] != float('inf') and dist[i] + times[i][j] < dist[j]:
                    return True, [x for x in range(len(times) - 2)]
        return False, dist
    
    distArr = []
    for i in range(len(times)):
        neg, d = BellmanFord(i)
        if neg:
            return d
        distArr.append(d)

    # Debug
    loop = [0,0,0,0]
    stuf = []

    # goods = []
    maxSol = [0, []]
    # maxLen = [0]
    # maxArr = []
    # State tracker - current, visited, time
    stateTracker = []
    def dfs(path):
        # Debug
        loop[0] += 1
        # Just in case
        if len(path) > 12:
            # Debug
            loop[1] += 1
            return
        # Current location
        s = path[-1]
        # Calculate current length
        curr_len = 0
        for i in range(len(path) - 1):
            curr_len += distArr[path[i]][path[i+1]]
        
        # Good path --> reaches destination under time limit
        if s == len(times) - 1 and curr_len <= times_limit:
            if len(set(path)) > maxSol[0] or (len(set(path)) == maxSol[0] and sum(set(path)) < sum(maxSol[1])):
                maxSol[0] = len(set(path))
                maxSol[1] = list(set(path))
            # goods.append(path)
        # Bad path --> at destination but over time limit
        if s == len(times) - 1 and curr_len > times_limit:
            return
        # Bad path --> No way to get to destination
        # if curr_len + distArr[s] > times_limit:
        #     # Debug
        #     print(path)
        #     loop[2] += 1
        #     return
        # State tracker
        state = (s, set(path[:-1]), curr_len)
        if state in stateTracker:
            # Debug
            loop[3] += 1
            return
        stateTracker.append(state)

        # Debug
        stuf.append(path + [curr_len])

        # DFS through all possible children
        for i in range(len(times)):
            # Don't go to yourself
            if i == s or i in path:
                continue
            # Can't reach destination
            elif (curr_len + distArr[s][i] + distArr[i][-1] > times_limit):
                continue
            # Circular loop
            elif distArr[s][i] + distArr[i][s] == 0 and i in path and s in path[:-1]:
                continue
            else:
                dfs(path + [i])
    dfs([0])

    # maxLen = 0
    # maxArr = []
    # for g in goods:
    #     if len(set(g)) > maxLen or (len(set(g)) == maxLen and sum(set(g)) < sum(maxArr)):
    #         maxLen = len(set(g))
    #         maxArr = list(set(g))
    maxArr = sorted([i-1 for i in maxSol[1][1:-1]])

    # Debug
    print(loop)
    with open('tmp.txt', 'w') as f:
        for xs in stuf:
            tm = ','.join([str(pp) for pp in xs])
            f.write(f'[{tm}]\n')
    return maxArr

    '''SEE MY STRUGGLE BELOW'''
    
    # goods = []     
    # # BFS
    # queue = []
    # queue.append([0])
    # while queue:
    #     path = queue.pop(0)
    #     if len(path) > 12:
    #         break
    #     # Calculate current length
    #     curr_len = 0
    #     for i in range(len(path) - 1):
    #         curr_len += times[path[i]][path[i+1]]
    #     # Determine if this path is good
    #     if path[-1] == len(times) - 1:
    #         if curr_len <= times_limit:
    #             goods.append(path)
    #         else:
    #             continue

    #     for i in range(len(times)):
    #         # Most recent point
    #         if i == path[-1]:
    #             continue
    #         # Unreachable
    #         if curr_len + times[path[-1]][i] + distArr[i] > times_limit:
    #             continue
    #         queue.append(path + [i])

    # maxLen = 0
    # maxArr = []
    # for g in goods:
    #     if len(set(g)) > maxLen:
    #         maxLen = len(set(g))
    #         maxArr = [sorted(list(set(g)))]
    #     elif len(set(g)) == maxLen:
    #         maxArr.append(sorted(list(set(g))))
    # maxArr.sort()
    # res = sorted([i-1 for i in maxArr[0][1:-1]])
    # return res

    


    # # Bellman Ford
    # dist = [float("Inf")] * len(times)
    # dist[0] = 0
    
    # for _ in range(len(times)):
    #     for i in range(len(times)):
    #         for j in range(len(times)):
    #             dist[j] = min(dist[i] + times[i][j], dist[j])

    # for i in range(len(times)):
    #     for j in range(len(times)):
    #         if dist[i] + times[i][j] < dist[j]:
    #             return [x for x in range(len(times) - 2)]

    # # def getCycle(path):
    # #     for size in range(2, len(times)):
    # #         if size > len(path):
    # #             return False
    # #         p = set()
    # #         for i in range(len(path) - size + 1):
    # #             arr = tuple(path[i:i+size])
    # #             if arr in p:
    # #                 return True
    # #             p.add(arr)
    # #     return False
    # # Debug
    # loop = [0, 0]
    # stuf = []
    # # DFS
    # goods = []
    # State tracker - current, visited, time
    # stateTracker = []
    # '''
    # 0 1 2 3 --> test 1,2,3,4,5
    # IF goes over --> bad and skip
    # IF you've visited it already and it's in 2,3,4 --> skip
    # IF you're at 5 --> good, add to solution set, recurse
    # ELSE --> recurse
    # '''
    # def dfs(path):
    #     '''
    #     Longest path:
    #     1 7 2 7 3 7 4 7 5 7 6 7
    #     '''
        # # Debug
        # loop[0] += 1
    #     # Just in case
    #     if len(path) > 19:
    #         # Debug
    #         loop[1] += 1
    #         return
    #     # Current location
    #     s = path[-1]
    #     # Calculate current length
    #     curr_len = 0
    #     for i in range(len(path) - 1):
    #         curr_len += times[path[i]][path[i+1]]
    #     if s == len(times) - 1 and curr_len <= times_limit:
    #         goods.append(path)
    #     if (s == len(times) - 1 and curr_len > times_limit) or (curr_len > 999):
    #         return
    #     # if getCycle(path):
    #     #     return
    #     # State tracker
    #     state = (s, set(path[:-1]), curr_len)
    #     if state in stateTracker:
    #         return
    #     stateTracker.append(state)
    #     # Debug
    #     stuf.append(state)
    #     for i in range(1, len(times)):
    #         # Don't go to yourself
    #         if i == s:
    #             continue
    #         if s in path[:-1] and i in path:
    #             continue
    #         # if getCycle(path + [i]):
    #         #     continue
    #         dfs(path + [i])
    # dfs([0])
    # maxLen = 0
    # maxArr = []
    # for g in goods:
    #     if len(set(g)) > maxLen:
    #         maxLen = len(set(g))
    #         maxArr = list(set(g))
    # maxArr = sorted([i-1 for i in maxArr[1:-1]])
    # # Debug
    # print(loop)
    # with open('tmp.txt', 'w') as f:
    #     for xs in stuf:
    #         tm = ','.join([str(pp) for pp in xs])
    #         f.write(f'[{tm}]\n')
    # return maxArr
    

x = solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
print(f'1: {x}')
'''
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0

0 1
'''

z = solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [-1, 3, 2, 2, 0]], 1)
print(f'2: {z}')
'''
0 1 2
'''

a = solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
print(f'3: {a}')
'''
1 2
'''

y = solution(
    [
        [0, 2, -1, 2, -1], 
        [-1, 0, 2, 2, 10], 
        [9, 3, 0, 1, -1], 
        [9, 3, 2, 0, 10], 
        [9, 3, 2, 2, 0]
    ], 100)
print(f'4: {y}')
'''
0 2 -1 2 -1
-1 0 2 2 10
9 3 0 1 -1
9 3 2 0 10
9 3 2 2 0

0 1 -1 0 -2
-1 0 -2 -1 3
1 2 0 1 -1
2 3 1 0 0
2 3 1 2 0

0 1 0 2 3 4

0 1 2
'''
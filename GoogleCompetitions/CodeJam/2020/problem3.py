tc = int(input())

for i in range(tc):
    n = int(input())
    task = []
    for j in range(n):
        task.append(list(map(int, input().split(' ') + [int(j)])))
    
    res = ''
    cend, jend = 0, 0
    task.sort(key=lambda x: x[0])
    for j, t in enumerate(task):
        if t[0] >= cend:
            cend = t[1]
            task[j].append('C')
            continue
        if t[0] >= jend:
            jend = t[1]
            task[j].append('J')
            continue
        res = 'IMPOSSIBLE'
        break
    else:
        task.sort(key=lambda x:x[2])
        res = ''.join([t[3] for t in task])

    print('Case #{}: {}'.format(i+1, res))

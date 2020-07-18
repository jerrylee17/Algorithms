tc = int(input())

for i in range(tc):
    n = int(input())
    arr = []
    # load up array
    k, r, c = 0, 0, 0
    for j in range(n):
        tmp = list(map(int, input().split(' ')))
        arr.append(tmp)
        if len(set(tmp)) != n:
            r += 1
    
    for x in range(n):
        if len(set([row[x] for row in arr])) != n:
            c += 1
        k += arr[x][x]
    print('Case #{}: {} {} {}'.format(i+1, k, r, c))
    

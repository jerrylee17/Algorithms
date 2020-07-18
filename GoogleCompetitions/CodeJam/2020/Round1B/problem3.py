tc = int(input())

def mix(r, s):
    res = []
    sli = r*s - 1
    for i in range(r-1, 0, -1):
        for j in range(s-1, 0, -1):
            tmp = str(sli-i) + ' ' + str(i)
            res.append(tmp)
            sli -= 1
        sli -= 1
    return res
    

for i in range(tc):
    r, s = list(map(int, input().split(' ')))
    res = mix(r,s)
    print('Case #{}: {}'.format(i+1, len(res)))
    [print(x) for x in res]

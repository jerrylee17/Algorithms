import math
tc = int(input())

def jump(curr, target, i, res):
    if list(target) == curr:
        return res
    power = 2**i
    if (target[0] - curr[0]) % power != 0:
        return False
    elif (target[1]-curr[1]) % power != 0:
        return False
    maxiter = math.log(abs(target[0])+abs(target[1]), 2)+1
    if i > maxiter: return False
    # next = []
    # while True:
    j = [0,0,0,0]
    tmp = [curr[0]+power, curr[1]]
    j[0] = jump(tmp, target, i + 1, res + 'E')
    tmp = [curr[0]-power, curr[1]]
    j[1] = jump(tmp, target, i + 1, res + 'W')
    tmp = [curr[0], curr[1]+power]
    j[2] = jump(tmp, target, i + 1, res + 'N')
    tmp = [curr[0], curr[1]-power]
    j[3] = jump(tmp, target, i + 1, res + 'S')
    j = list(filter(lambda x: (x != False), j))
    if not j:
        return False
    return min(j, key=lambda x: len(x))



for i in range(tc):
    target = tuple(map(int, input().split(' ')))
    curr = [0, 0]
    res = ''
    res = jump(curr, target, 0, res)
    if not res:
        res = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(i+1, res))


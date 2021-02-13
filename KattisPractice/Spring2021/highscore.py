from math import ceil
tc = int(input())

'''
Algorithm:
MAKE c = smallest
(a+x)**2 + (b+y)**2 + (c+z)**2 + 7*(c+z)
x + y + z = n
You either add all to the largest or you try to balance them
a**2 to (a+1)**2: 2a+1
2a+1 vs 2c+1 + 7*c
'''

def calcScore(a):
    return a[0]**2 + a[1]**2 + a[2]**2 + a[2]*7

def solve(a, w):
    # Add all to largest
    l = calcScore([a[0]+w, a[1], a[2]])
    diffs = [a[0]-a[1], a[1]-a[2]]
    # balance out 
    if w < diffs[1]:
        s = calcScore([a[0], a[1], a[2] + w])
        return max(l, s)
    a[2] += diffs[1]
    w -= diffs[1]
    # a[1] = a[2] at this point
    m = calcScore([a[0]+w, a[1], a[2]])
    if w < diffs[0]*2:
        s = calcScore([a[0], a[1] + ceil(w/2), a[2] + w//2])
        return max([l, m, s])
    a[1] += diffs[0]
    a[2] += diffs[0]
    w -= diffs[0]*2
    # a[1] = a[2] = a[3]
    c = calcScore([a[0]+w, a[1], a[2]])
    div, rem = w // 3, w % 3
    a[0] += div
    a[1] += div
    a[2] += div
    for i in range(rem):
        a[i] += 1
    s = calcScore(a)
    return max([l, m, c, s])

    # for i in range(w):
        # Determine who to add 1 to
        

for _ in range(tc):
    *a,w = list(map(int, input().split(' ')))
    # Highest to lowest
    a.sort(reverse=True)
    res = solve(a, w)
    print(res)
    
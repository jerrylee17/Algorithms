n, m, p = list(map(int, input().split(' ')))

children = []
for _ in range(n):
    k, *i = list(map(int, input().split(' ')))
    children.append(i)

categories = []
for _ in range(p):
    l, *t, r = list(map(int, input().split(' ')))
    categories.append([r, t])

'''
Algorithm:
Distribute out categories first. 
'''

import functools
s1, s2 = [], []
for i in range(3):
    a, b = list(map(int, input().split(' ')))
    s1.append(a)
    s2.append(b)

res1 = functools.reduce(lambda x, y: x ^ y, s1)
res2 = functools.reduce(lambda x, y: x ^ y, s2)
print(res1, res2)

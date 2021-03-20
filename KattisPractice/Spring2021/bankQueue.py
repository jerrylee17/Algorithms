n, t = list(map(int, input().split()))
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))


'''
(1200, 0)
(1000, 1)
(2000, 2)
(500, 2)
'''

people.sort(key=lambda x: (x[1], x[0]), reverse=True)
cs = 0
for i in range(t - 1, -1, -1):
    sta = []
    for j, e in enumerate(people):
        if i > e[1]:
            break
        sta.append(e)
    if not sta:
        continue
    biggest = max(sta, key=lambda x: x[0])
    cs += biggest[0]
    people.pop(people.index(biggest))
print(cs)

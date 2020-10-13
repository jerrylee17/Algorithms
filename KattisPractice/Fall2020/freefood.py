n = int(input())

events = []

for _ in range(n):
    a, b = list(map(int, input().split(' ')))
    tmp = [x for x in range(a, b+1)]
    events.extend(tmp)

events = list(set(events))
print(len(events))

import math
tc = int(input())

# load everything in
actions = {}
for i in range(tc):
    t, d = list(map(int,input().split(' ')))

    for i in [d, d-t, d-2*t]:
        actions[i] = dict.get(actions, i, 0) + 1

print(math.ceil(max(actions.values())/2))

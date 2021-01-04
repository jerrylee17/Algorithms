tc = int(input())

room = set()
for _ in range(tc):
    action, name = input().split(' ')
    if action == 'entry':
        res = f'{name} entered'
        if name in room:
            res += ' (ANOMALY)'
        else:
            room.add(name)
        print(res)
    else:
        res = f'{name} exited'
        if name not in room:
            res += ' (ANOMALY)'
        else:
            room.remove(name)
        print(res)

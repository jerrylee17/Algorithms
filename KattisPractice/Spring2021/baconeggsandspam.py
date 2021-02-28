for _ in range(100):
    c = int(input())
    if c == 0:
        break
    logs = {}
    for i in range(c):
        name, *items = input().split()
        for item in items:
            logs[item] = sorted(logs.get(item, []) + [name])
    for key, value in sorted(logs.items(), key=lambda x: x[0]):
        res = key + ' ' + ' '.join(value)
        print(res)
    print()

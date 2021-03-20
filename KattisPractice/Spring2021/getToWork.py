c = int(input())
for case in range(c):
    n, t = list(map(int, input().split()))
    e = int(input())
    employees = []
    for i in range(e):
        h, p = list(map(int, input().split()))
        if h == t:
            continue
        employees.append((h-1,p))
    towns = [0 for i in range(0, n)]
    # employees.sort(lambda x: (x[0], 0-x[1]))
    d = {i: [] for i in range(n)}
    for e in employees:
        d[e[0]].append(e[1])
    # towns = []
    imp = False
    for town, cars in sorted(d.items()):
        if town == t-1:
            continue
        if not cars:
            continue
        cars.sort(reverse=True)
        subt = 0
        for i, c in enumerate(cars):
            subt += c
            if subt >= len(cars):
                towns[town] = i+1
                break
        else:
            imp = True
            break
    res = ' '.join(list(map(str, towns)))
    if imp:
        print(f'Case #{case+1}: IMPOSSIBLE')
    else:
        print(f'Case #{case+1}: {res}')
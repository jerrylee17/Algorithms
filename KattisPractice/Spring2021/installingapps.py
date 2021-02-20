n, c = list(map(int, input().split()))
apps = []
for i in range(n):
    d, s = list(map(int, input().split()))
    apps.append((d, s, i+1))
apps.sort(key=lambda x: x[1])

def greedy(space, apps):
    downloads = []
    for d, s, i in apps:
        if s > space:
            break
        if d <= space:
            space -= s
            downloads.append(i)
    print(len(downloads))
    if downloads:
        print(' '.join([str(d) for d in downloads]))

greedy(c, apps)
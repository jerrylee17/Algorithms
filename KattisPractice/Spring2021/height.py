tc = int(input())

for t in range(tc):
    s = list(map(int, input().split()))[1:]
    res = 0
    for i, e in enumerate(s):
        for j in range(i-1, -1, -1):
            if e < s[j]:
                s[j+1], s[j] = s[j], s[j+1]
                res += 1
            else:
                break
    print(f'{t+1} {res}')

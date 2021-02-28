n = int(input())

for _ in range(n):
    g = list(map(int, input().split()))
    g = g[1:]
    for i in range(1, len(g) - 1):
        gx = g[:i] + g[i+1:]
        if sorted(gx) == gx:
            print(i+1)
            break
    # prev = g[0]
    # for i, e in enumerate(g[:-1]):
    #     if i == 0:
    #         continue
    #     if not prev < e < g[i+1]:
    #         try:
    #             if e < g[i+2]:
    #                 print(i+2)
    #                 break
    #         except:
    #             print(i+1)
    #             break
    #         print(i+1)
    #         break
    #     prev = e

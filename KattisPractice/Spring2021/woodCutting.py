tc = int(input())

for _ in range(tc):
    n = int(input())
    cust = []
    for i in range(n):
        cust.append(sum(list(map(int, input().split()))[1:]))
    cust.sort()
    tot = 0
    for i, c in enumerate(cust):
        tot += c * (len(cust) - i)
    print(tot / len(cust))
        


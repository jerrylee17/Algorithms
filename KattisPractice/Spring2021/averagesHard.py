tc = int(input())

for i in range(tc):
    blank = input()
    ncs, ne = list(map(int, input().split()))
    cs = list(map(int, input().split()))
    e = list(map(int, input().split()))
    acs = sum(cs) / len(cs)
    ae = sum(e) / len(e)
    n = list(filter(lambda x: ae < x < acs, cs))
    print(len(n))

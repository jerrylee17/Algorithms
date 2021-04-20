def solve(cj, jc, s):
    s = s.replace('?', '')
    if not s:
        return 0
    cost = 0
    prev = s[0]
    for c in s[1:]:
        if c != prev:
            if prev == 'C':
                cost += cj
            else:
                cost += jc
        prev = c
    return cost

for i in range(int(input())):
    cj, jc, s = input().split()
    cj = int(cj)
    jc = int(jc)
    res = solve(cj, jc, s)
    print(f'Case #{i+1}: {res}')

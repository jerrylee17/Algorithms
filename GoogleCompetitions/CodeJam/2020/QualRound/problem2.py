tc = int(input())

for i in range(tc):
    s = input()
    res = ''
    curr = 0
    for c in s:
        if int(c) == curr:
            res += c
        elif int(c) > curr:
            res += ('(' *(int(c)-curr)) + c
            curr = int(c)
        else:
            res += (')' *(curr-int(c))) + c
            curr = int(c)
    res += ')'*curr
    print('Case #{}: {}'.format(i+1, res))
        

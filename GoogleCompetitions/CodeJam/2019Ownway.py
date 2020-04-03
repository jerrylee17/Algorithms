tc = int(input())

for i in range(tc):
    x, y = input(), input()
    s = ''
    for c in y:
        if c == 'E':
            s += 'S'
        else:
            s += 'E'
    print('Case #{}: {}'.format(i+1, s))
    
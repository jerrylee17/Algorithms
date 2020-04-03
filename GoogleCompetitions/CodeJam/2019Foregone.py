tc = int(input())

for i in range(tc):
    x = input()
    res1, res2 = '', ''
    for c in x:
        if c == '4':
            res1 += '3'
            res2 += '1'
        else:
            res1 += c
            res2 += '0'
    res2 = res2.lstrip('0')
    print("Case #{}: {} {}".format(i+1,res1, res2))
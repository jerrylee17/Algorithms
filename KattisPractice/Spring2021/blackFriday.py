from collections import Counter

n = int(input())
die = list(map(int, input().split()))
c = Counter(die)
p = sorted(c.items(), key=lambda x: (x[1], 0-x[0]))[0]
if p[1] != 1:
    print('none')
else:
    print(die.index(p[0]) + 1)



    

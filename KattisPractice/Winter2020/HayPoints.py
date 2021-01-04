m, n = list(map(int, input().split(' ')))

hayMap = {}
for i in range(m):
    key, val = input().split(' ')
    hayMap[key] = int(val)

for i in range(n):
    subtotal = 0
    while True:
        line = input()
        if line == '.':
            print(subtotal)
            break
        for word in line.split(' '):
            subtotal += hayMap.get(word, 0)

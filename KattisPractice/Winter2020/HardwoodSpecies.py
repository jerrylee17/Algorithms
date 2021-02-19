import sys

trees = {}
total = 0
for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    trees[line] = trees.get(line, 0) + 1
    total += 1

sol = sorted(trees.items(), key=lambda x: x[0])
sol = list(map(lambda x: [x[0], x[1]*100/total], sol))
for item in sol:
    print(f'{item[0]} {round(item[1], 6)}')

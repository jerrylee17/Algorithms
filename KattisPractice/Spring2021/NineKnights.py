solvable = True
knights = []
for i in range(5):
    row = input()
    for j, c in enumerate(row):
        if not solvable:
            break
        if c == 'k':
            for k in knights:
                if (abs(k[0]-i) == 1 and abs(k[1]-j) == 2) or (abs(k[0]-i) == 2 and abs(k[1]-j) == 1):
                    solvable = False
            knights.append((i, j))
if len(knights) != 9:
    solvable = False

result = 'valid' if solvable else 'invalid'
print(result)

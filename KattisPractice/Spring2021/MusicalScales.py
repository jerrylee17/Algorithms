scaleConversion = {
    'A': 0,
    'A#': 1,
    'B': 2,
    'C': 3,
    'C#': 4,
    'D': 5,
    'D#': 6,
    'E': 7,
    'F': 8,
    'F#': 9,
    'G': 10,
    'G#': 11
}
numConversion = {v: k for k, v in scaleConversion.items()}

def checkScale(n, arr):
    availableNums = set([])
    for i in range(7):
        availableNums.add(n)
        if i == 2 or i == 6:
            n += 1
        else:
            n += 2
        n %= 12
    for a in arr:
        if scaleConversion[a] not in availableNums:
            return False
    return True

notes = int(input())
arr = set(input().split())
res = []
for i in range(12):
    if checkScale(i, arr):
        res.append(i)
result = []
for r in res:
    result.append(numConversion[r])

if not result:
    print('none')
else:
    print(' '.join(result))

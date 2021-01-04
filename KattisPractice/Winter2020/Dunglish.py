n = int(input())
sentence = input().split(' ')
m = int(input())

# words = []
goodDict = {}
allDict = {}
for _ in range(m):
    w = input().split(' ')
    if w[2] == 'correct':
        goodDict[w[0]] = goodDict.get(w[0], []) + [w[1]]
    allDict[w[0]] = allDict.get(w[0], []) + [w[1]]


# Getting corrects
corrects = 1
for word in sentence:
    corrects *= len(goodDict.get(word, []))

# Getting incorrects
incorrects = 1
for word in sentence:
    incorrects *= len(allDict.get(word, []))
incorrects -= corrects

# None correct
if corrects == 0 and incorrects == 1:
    res = ''
    for word in sentence:
        res += allDict[word][0] + ' '
    print(res)
    print('incorrect')
# Only 1 correct
elif corrects == 1 and incorrects == 0:
    res = ''
    for word in sentence:
        res += goodDict[word][0] + ' '
    print(res)
    print('correct')
else:
    print(f'{corrects} correct')
    print(f'{incorrects} incorrect')

def checkSides(a, b, c):
    sides = [a, b, c]
    hypo = max(sides)
    sides.pop(sides.index(hypo))
    result = "right" if sides[0]**2 + sides[1]**2 == hypo**2 else "wrong"
    print(result)


while True:
    a, b, c = list(map(int, input().split(' ')))
    if a == 0 and b == 0 and c == 0:
        break
    checkSides(a, b, c)

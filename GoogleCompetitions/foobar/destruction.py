import math


def solution(pegs):
    # Your code here
    '''
    len(pegs) = 3: 
    a + 2b + c = p2 - p0
    a + b = p1 - p0
    b + c = p2 - p1
    a = 2c
    a = 2(p2-p1-b) = 2(p2-p1-(p1-p0-a)) = 2(p2-2p1+p0+a)
    a = 2(-p0+2p1-p2)

    len(pegs) = 4:
    a + 2b + 2c + d = p3 - p0
    a = 2/3 * (-p0 + 2(p1-p2) + p3)

    Odd: 
    a = 2 * (-p0 + 2(p1-p2+p3...) -p(n-1))

    Even:
    a = 2/3 * (-p0 + 2(p1-p2+p3-p4...) + p(n-1))

    '''
    def simplify(top, bottom):
        div = math.gcd(top, bottom)
        return [top // div, bottom // div]

    def calcOdd(peg):
        res = 0
        for i, e in enumerate(peg):
            if i == 0:
                res -= e
                continue
            if i == len(peg) - 1:
                res -= e
                continue
            if i % 2 == 1:
                res += 2*e
            elif i % 2 == 0:
                res -= 2*e
        return [2 * res, 1]

    def calcEven(peg):
        res = 0
        for i, e in enumerate(peg):
            if i == 0:
                res -= e
                continue
            if i == len(peg) - 1:
                res += e
                continue
            if i % 2 == 1:
                res += 2*e
            elif i % 2 == 0:
                res -= 2*e
        return [2 * res, 3]

    def errorCheck(a, peg):
        currPos = peg[0] + a
        for p in peg[1:]:
            if currPos >= p:
                return True
            diff = p - currPos
            currPos += 2 * diff
        return False

    # Corner case: 0, 1
    if len(pegs) <= 1:
        return [-1, -1]

    # Corner case: 2
    if len(pegs) == 2:
        # 2/3 (p[1] - p[0])
        top = (pegs[1] - pegs[0]) * 2
        bottom = 3
        fraction = simplify(top, bottom)
        return fraction

    res = [0, 0]
    if len(pegs) % 2 == 0:
        res = calcEven(pegs)
    elif len(pegs) % 2 == 1:
        res = calcOdd(pegs)

    if res[0] <= 0:
        return [-1, -1]

    if (errorCheck(res[0]/res[1], pegs)):
        return [-1, -1]

    res = simplify(res[0], res[1])
    return res


print(solution([4, 30, 50]))

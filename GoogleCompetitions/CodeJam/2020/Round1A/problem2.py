tc = int(input())

def genTriangle():
    triangle = [[0 for i in range(50)] for j in range(50)]
    triangle[0][0] = 1
    for r in range(1, len(triangle)):
        for c in range(r + 1):
            if c == 0: 
                triangle[r][c] = 1
                continue
            triangle[r][c] = triangle[r-1][c-1] + triangle[r-1][c]
    return triangle

def traverseTriangle(target, triangle, CurrPos, CurrSum):
    arr = []
    mirror = target // 2

    CurrSum += triangle[CurrPos[0]][CurrPos[1]]
    print(CurrPos[0], CurrPos[1])
    if CurrSum < mirror:
        traverseTriangle()
        


for i in range(tc):
    target = int(input())
    triangle = genTriangle()
    traverseTriangle(target, triangle, [1, 1], 0)
import pprint


def findNext(board, currPos, targetChar):
    possiblePositions = [
        (currPos[0] + 1, currPos[1] - 2),
        (currPos[0] + 1, currPos[1] + 2),
        (currPos[0] - 1, currPos[1] - 2),
        (currPos[0] - 1, currPos[1] + 2),
        (currPos[0] + 2, currPos[1] - 1),
        (currPos[0] + 2, currPos[1] + 1),
        (currPos[0] - 2, currPos[1] - 1),
        (currPos[0] - 2, currPos[1] + 1),
    ]
    result = []
    for elem in possiblePositions:
        x, y = elem
        try:
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                continue
            if board[x][y] == targetChar:
                result.append(elem)
        except:
            continue
    return result


dimensions = int(input())
board = input()
'''
IXIXX
XXCXA
XSXXP
XXCSX
AGXXX
'''
board = [board[dimensions*n:dimensions*(n+1)] for n in range(dimensions)]
targetString = 'ICPCASIASG'
# Base case
# posArray: (x,y,targetIndex)
posArray = [(ix, iy, 1) for ix, row in enumerate(board)
            for iy, elem in enumerate(row) if elem == targetString[0]]


def findString(board, targetString, posArray):
    while posArray:
        x, y, i = posArray.pop()
        if i == len(targetString):
            print('YES')
            return
        nextPositions = findNext(board, (x, y), targetString[i])
        nextPositions = [elem + (i+1,) for elem in nextPositions]
        posArray.extend(nextPositions)
    print('NO')
    return


findString(board, targetString, posArray)

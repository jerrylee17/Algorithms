# board = []
queenCoords = []
for x in range(8):
    row = input()
    for y, e in enumerate(row):
        if e == '*':
            queenCoords.append((x, y))

def solve(qc):
    # if len(qc) > 8:
    #     print('invalid')
    #     return
    for i in range(len(qc)):
        for j in range(i+1, len(qc)):
            # same row
            if qc[i][0] == qc[j][0]:
                print('invalid')
                return
            # same col
            if qc[i][1] == qc[j][1]:
                print('invalid')
                return
            # same diagonal
            if abs(qc[i][0] - qc[j][0]) == abs(qc[i][1] - qc[j][1]):
                print('invalid')
                return
    print('valid')
    return

solve(queenCoords)
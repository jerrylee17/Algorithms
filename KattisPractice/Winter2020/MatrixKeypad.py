tc = int(input())


def solve(mat):
    res = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
    # if not checkBoard(mat):
    #     print('impossible')
    #     return
    for i, r in enumerate(mat):
        for j, e in enumerate(r):
            if e == '0':
                res[i][j] = 'N'
                if (r.count('1') >= 1 and
                        [row[j] for row in mat].count('1') >= 1):
                    print('impossible')
                    return
            else:
                # It is the only one in its row/col
                if (r.count('1') == 1 or
                        [row[j] for row in mat].count('1') == 1):
                    res[i][j] = 'P'
                else:
                    res[i][j] = 'I'
    for row in res:
        print(''.join(row))
    return


for _ in range(tc):
    r, c = list(map(int, input().split(' ')))
    mat = []
    for i in range(r):
        mat.append(input())
    solve(mat)
    print('----------')

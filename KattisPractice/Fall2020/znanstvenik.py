r, c = list(map(int, input().split(' ')))


def isValid(mat):
    if not mat:
        return False
    cols = set([''.join([
        mat[i][j] for i in range(len(mat))
    ]) for j in range(len(mat[0]))])

    if len(cols) != len(mat[0]):
        return False
    return True


def calcRows(mat):
    r = len(mat)
    l = 0
    while l < r:
        m = l + (r - l) // 2
        if isValid(mat[m:]) and not isValid(mat[m+1:]):
            return m
        elif isValid(mat[m:]) and isValid(mat[m+1:]):
            l = m + 1
        else:
            r = m - 1
    return l


mat = []
for i in range(r):
    mat.append(input())

res = calcRows(mat)
print(res)

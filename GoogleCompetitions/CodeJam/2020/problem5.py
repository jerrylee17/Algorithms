tc = int(input())

# Split k into a sum of 3 that doesn't have all but 1 of the same #
def genDiag(n, k):
    # 100% Fail cases
    if k > (n**2) or k < n:
        return False
    if k == n + 1 or k == n**2 - 1:
        return False
    # generate diagonals
    if k % n != 1 and k % n != n - 1:
        tmp = [k//n + 1 for i in range(k % n)]
        tmp.extend([k//n for i in range(n-(k%n))])
        return tmp
    # get rid of corner cases
    if k % n == 1:
        # pop a value in first
        tmp = [k//n-1]
        # set k and n
        k -= tmp[0]
        n -= 1
        tmp.extend([k//n + 1 for i in range(k % n)])
        tmp.extend([k//n for i in range(n-(k%n))])
        return tmp
    # pop a value in first
    tmp = [k//n+2]
    # set k and n
    k -= tmp[0]
    n -= 1
    tmp.extend([k//n + 1 for i in range(k % n)])
    tmp.extend([k//n for i in range(n-(k%n))])
    return tmp

def checkRow(arr, row, num, n): 
    for i in range(n): 
        if(arr[row][i] == num): 
            return True
    return False

def checkCol(arr, col, num, n): 
    for i in range(n): 
        if(arr[i][col] == num): 
            return True
    return False

def checkSafe(arr, row, col, num, n ): 
    return not checkRow(arr, row, num, n) and not checkCol(arr, col, num, n)

def getEmpty(arr, l, n):
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 0:
                l[0], l[1] = r, c
                return True
    return False

def fillSquare(arr):
    n = len(arr)
    # position of where we're checking
    l=[0,0] 
    if(not getEmpty(arr, l, n)): 
        return True
    row=l[0] 
    col=l[1] 
    for num in range(1, n+1): 
        if(checkSafe(arr, row, col, num, n)): 
            arr[row][col]=num 
            if(fillSquare(arr)): 
                return True
            arr[row][col] = 0
    return False 

def genSquare(diagonals):
    n = len(diagonals)
    square = [[0 for i in range(n)] for j in range(n)]
    # set diagonals
    for i in range(n):
        square[i][i] = diagonals[i]
    if fillSquare(square):
        return square
    return False

for i in range(tc):
    n, k = list(map(int, input().split(' ')))
    res = ''
    diagonal = genDiag(n, k)
    if not diagonal:
        print('Case #{}: IMPOSSIBLE'.format(i+1))
        continue
    square = genSquare(diagonal)
    if not square:
        print('Case #{}: IMPOSSIBLE'.format(i+1))
        continue
    print('Case #{}: POSSIBLE'.format(i+1))
    [print(*row) for row in square]

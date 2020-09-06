def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6
    return True

n, b = list(map(int,input().split(' ')))
if n ** 2 > b:
    print('impossible')
    exit()
choices = list(range(1, b + 1))
def addNum(matrix, choicesLeft, curSum):
    if len(matrix) == n and len(matrix[-1]) == n:
        return checkMatrix(matrix)
    else:
        for c in choicesLeft:
            newMatrix = matrix.copy()
            newChoices = choicesLeft.copy()
            newChoices.remove(c)
            if len(matrix) == 0:
                temp = [c]
                newMatrix.append(temp)
                a = addNum(newMatrix, newChoices, c)
                if a:
                    return a
            else:
                if len(newMatrix[-1]) + 1 == n and isPrime(curSum + c):
                    newMatrix[-1].append(c)
                    temp = [c]
                    newMatrix.append(temp)
                    a = addNum(newMatrix, newChoices, 0)
                    if a:
                        return a
                else:
                    newMatrix[-1].append(c)
                    a = addNum(newMatrix, newChoices, curSum + c)
                    if a:
                        return a
        return False
def checkMatrix(matrix):
    cols = [0 for i in range(len(matrix))]
    for row in matrix:
        cols[0] += row[0]
        cols[1] += row[1]
        cols[2] += row[2]
    valid = True
    for c in cols:
        if not isPrime(c):
            valid = False
            break
    if valid:
        return matrix
    return valid

ans = addNum([], choices,0)
if ans:
    for r in ans:
        print(r)
else:
    print('impossible')

def solution(x, y):
    x = long(x)
    y = long(y)
    count = 0
    while not (x == 1 and y == 1):
        # Exit condition
        if x == y or x < 1 or y < 1:
            return 'impossible'
        elif x == 1:
            count += y - 1
            break
        elif y == 1:
            count += x - 1
            break
        elif x > y:
            count += x // y
            x = x % y
        else:
            count += y // x
            y = y % x
    return str(count)


s = solution('4', '7')
print(s)

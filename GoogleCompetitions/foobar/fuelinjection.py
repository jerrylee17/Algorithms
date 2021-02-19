def solution(n):
    n = long(n)
    count = 0
    while n > 3:
        count += 1
        if not n & 1:
            n /= 2
        else:
            if n & 2:
                count += 1
                n += 1
                n /= 2
            else:
                count += 1
                n -= 1
                n /= 2
    if n == 3:
        count += 2
    elif n == 2:
        count += 1
    return count


x = solution('4')
print(x)

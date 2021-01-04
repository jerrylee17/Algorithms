def solve(code, guess):
    c = sorted(code)
    g = sorted(guess)
    total = 0
    for g1 in g:
        if g1 in c:
            c.pop(c.index(g1))
            total += 1

    r = 0
    for c1, g1 in zip(code, guess):
        if c1 == g1:
            r += 1
    s = total - r
    return (r, s)


n, code, guess = input().split(' ')
r, s = solve(code, guess)
print(r, s)

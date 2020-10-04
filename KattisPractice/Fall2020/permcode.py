def calcd(x, n):
    return int(n**1.5 + x) % n


def charReplace(string, position, character):
    return string[:position] + character + string[position+1:]


def initPos(p, s, c, d):
    # Returns 1 charcter
    return p[s.find(c[d])]


def calcPos(p, s, c, currPos):
    # Assume you know currPos + 1
    ctpos = s.find(c[currPos])  # Index (2)
    nextpos = s.find(c[(currPos + 1) % len(c)])
    return p[ctpos ^ nextpos]


while True:
    x = int(input())
    if x == 0:
        break
    s = input()
    p = input()
    c = input()
    n = len(c)
    d = calcd(x, n)
    res = c
    # initial case
    res = charReplace(res, d, initPos(p, s, c, d))
    # Time to do the rest....
    for i in range(1, n):
        index = (d - i) % n
        pos = calcPos(p, s, res, index)
        res = charReplace(res, index, pos)
    print(res)

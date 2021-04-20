import functools

def solve(cards):
    hand = []
    for p, n in cards:
        hand.extend([p]*n)
    x = 0
    maxScore = 0
    while x < 2**len(hand):
        h1 = []
        h2 = []
        for i, e in enumerate(hand):
            if x & (2**(i)) == 0:
                h1.append(e)
            else:
                h2.append(e)
        if sum(h1) == functools.reduce(lambda x, y : x*y, h2, 1):
            maxScore = max(maxScore, sum(h1))
        x += 1
    return maxScore


for i in range(int(input())):
    m = int(input())
    cards = []
    for j in range(m):
        cards.append(list(map(int, input().split())))
    res = solve(cards)
    print(f'Case #{i+1}: {res}')



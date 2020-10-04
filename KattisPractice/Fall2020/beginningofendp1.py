from sys import stdin, stdout


def determineWinner(gLocations, bLocations):
    # True = G, False = B
    turn = True
    # positive = G, negative = B, 0 = S
    score = 0
    # gList = sorted(locations, key=lambda x: x[0], reverse=True)
    gLoc = gLocations.copy()
    bLoc = bLocations.copy()
    for _ in range(len(gLocations)):
        # G's turn
        if turn:
            # Find biggest
            biggest = max(gLoc)
            ind = gLoc.index(biggest)
            score += biggest
            bLoc.pop(ind)
            gLoc.pop(ind)
        else:
            # Find biggest
            biggest = max(bLoc)
            ind = bLoc.index(biggest)
            score -= biggest
            bLoc.pop(ind)
            gLoc.pop(ind)
        turn = not turn
    if score == 0:
        stdout.write('S\n')
    elif score > 0:
        stdout.write('G\n')
    elif score < 0:
        stdout.write('B\n')


# G goes first
gLocations = []
bLocations = []
n = int(input())
for _ in range(n):
    input = stdin.readline()
    g, b = list(map(int, input.split(' ')))
    gLocations.append(g)
    bLocations.append(b)
    determineWinner(gLocations, bLocations)
    stdout.flush()

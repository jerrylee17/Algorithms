n, m, d = list(map(int, input().split(' ')))

realRankings = {}

# Panda matches
for i in range(m):
    a, b = list(map(int, input().split(' ')))
    realRankings[a] = realRankings.get(a, 0) + 1
    realRankings[b] = realRankings.get(b, 0)

# Generate real rankings
realRankings = sorted(
    [(a, b) for a, b in realRankings.items()], key=lambda x: x[1], reverse=True
)

enteredRankings = []
for i in range(n):
    x = int(input())
    enteredRankings.append(x)

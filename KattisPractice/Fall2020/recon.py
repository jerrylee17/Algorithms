def calcDiff(vehicles):
    return max(v[0] for v in vehicles) - min(v[0] for v in vehicles)


def recon(vehicles):
    currDiff = calcDiff(vehicles)

    while True:
        vehicles = [
            [v[0]+v[1], v[1]]
            for v in vehicles
        ]
        nextDiff = calcDiff(vehicles)
        if calcDiff(vehicles) >= currDiff:
            return currDiff
        currDiff = nextDiff

    return currDiff


n = int(input())
vehicles = []

for i in range(n):
    info = list(map(int, input().split(' ')))
    vehicles.append(info)

result = recon(vehicles)
print(result)

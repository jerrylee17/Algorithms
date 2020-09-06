numfrogs, depth = tuple(map(int, input().split(' ')))

def froggys(frogs):
    # Determine which frog to eject
    dedFrog = ejectFrog(frogs)
    # Frog escaped. remove from list of frogs
    frogs.remove(dedFrog)
    if not dedFrog:
        return frogs
    return froggys(frogs)

def ejectFrog(frogs):
    # sort by leap capacity low to high
    leapfrogs = sorted(frogs, key: lambda a: a[0])

frogs = []
for i in range(numfrogs):
    frogs.append(
        list(map(int, input().split(' ')))
    )
    remaining = froggys(frogs)
    hopped = numfrogs - len(remaining)
    print(hopped)



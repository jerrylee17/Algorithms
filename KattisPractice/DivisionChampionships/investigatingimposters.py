n, imp = list(map(int, input().split()))
villagers = {}
peoples = []
susList = set()
for i in range(n):
    peeps = set(list(map(int, input().split()))[1:])
    # Initialize the set
    villagers[i+1] = villagers.get(i+1, set())
    for p in peeps:
        if i+1 in peeps:
            susList.add(i+1)
            break
        villagers[p] = villagers.get(p, set()) | {i+1}
    peoples.append(peeps)

# Confirmed imposters
queue = [s for s in susList]
while queue:
    # Everyone that voted for them is an imposter
    s = queue.pop()
    queue.extend(list(villagers[s]))
    susList |= set(villagers[s])
    villagers[s] = set()

# Discredit all imposter votes
for s in susList:
    for p in peoples[s-1]:
        try:
            villagers[p].remove(s)
        except:
            pass



for k, v in sorted(villagers.items(), key=lambda x: x[0]):
    if imp - len(susList) >= (n- len(susList)) // 2:
        print(0)
    elif k in susList:
        print(0)
    elif len(v) >= imp - len(susList):
        print(1)
    else:
        print(0)

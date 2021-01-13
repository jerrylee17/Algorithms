tc = int(input())

for _ in range(tc):
    n = int(input())
    if n == 0:
        print(0)
        continue
    gear = {}
    for i in range(n):
        item, category = input().split(' ')
        gear[category] = gear.get(category, 0) + 1
    total = 1
    for category, count in gear.items():
        total *= count + 1
    total -= 1
    print(total)

tc = int(input())

for _ in range(tc):
    cities = []
    c = int(input())
    for _ in range(c):
        cities.append(input())
    print(len(set(cities)))

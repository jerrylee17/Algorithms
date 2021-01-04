def solve(houses):
    # Sort from top to bottom
    houses.sort(key=lambda x: (x[0], x[1]))

    return


while True:
    n = int(input())
    if n == 0:
        break
    houses = []
    for i in range(n):
        h = list(map(float, input().split(' ')))
        houses.append(h)
    print(houses)
    solve(houses)
    space = input()

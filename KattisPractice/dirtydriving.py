n, p = list(map(int, input().split(' ')))

cars = sorted(list(map(int, input().split(' '))))

distances = [p*(i+1)-c + cars[0] for i,c in enumerate(cars)]

print(max(distances))

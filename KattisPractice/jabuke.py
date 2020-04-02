p1 = tuple(map(int, input().split(' ')))
p2 = tuple(map(int, input().split(' ')))
p3 = tuple(map(int, input().split(' ')))

def calcArea(p1, p2, p3):
    area = p1[0] * (p2[1]-p3[1]) + p2[0] * (p3[1]-p1[1]) + p3[0] * (p1[1]-p2[1])
    area = abs(area) / 2
    return area

area = (calcArea(p1, p2, p3))

tc = int(input())

count = 0
for i in range(tc):
    p = tuple(map(int, input().split(' ')))
    if (calcArea(p, p1, p2)) + (calcArea(p, p1, p3)) + (calcArea(p, p2, p3)) == area:
        count += 1

print(area)
print(int(count))

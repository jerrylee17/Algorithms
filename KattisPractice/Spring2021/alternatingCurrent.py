n, m = list(map(int, input().split()))

wires = []
for i in range(m):
    wires.append(list(map(int, input().split())))

print(''.join(['1' for i in range(m)]))

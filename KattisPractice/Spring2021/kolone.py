n1, n2 = list(map(int, input().split()))

c1 = input()
c1 = c1[::-1]
c2 = input()
seconds = int(input())

order = {}
# Reorder c1
for i, c in enumerate(c1):
    shift = seconds - (len(c1) - i) + 1
    pi = i + (shift > 0 and shift)
    order[c] = pi

tmp = {}
# Reorder c2
for i, c in enumerate(c2):
    shift = seconds - i
    pi = len(c1) + i - (shift > 0 and shift)
    tmp[c] = pi
order.update(tmp)
result = ''.join([x[0] for x in sorted([(c, i) for c, i in order.items()], key=lambda x: x[1])])
print(result)


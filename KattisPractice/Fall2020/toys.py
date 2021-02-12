t, k = list(map(int, input().split(' ')))

'''
(k-1) % t
(2k-1) % (t-1) = (2k-1 + (2k-1) // (t-1))
(3k-1) % (t-2)
((t-1)k-1) % 2
'''

# toys = [i for i in range(t)]

# pos = k-1
# while len(toys) > 1:
#     print(pos)
#     toys.pop(pos)
#     pos = (pos + k - 1) % len(toys)

pos = k - 1
div = 0
num = t
toys = [0 for _ in range(t)]
while num > 1:
    print(toys, num, div)
    toys[pos + div] = 1
    num -= 1
    div += (pos + k) // num
    pos = (pos + k) % num
    


print(toys.index(0))
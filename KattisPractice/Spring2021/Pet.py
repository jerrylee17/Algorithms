largest = 0
index = 0
for i in range(1, 6):
    me = sum(list(map(int, input().split())))
    if me > largest:
        index = i
        largest = me
print(f'{index} {largest}')


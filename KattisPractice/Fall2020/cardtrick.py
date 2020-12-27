tc = int(input())

'''
4
1: 2
2: 1
3: 4
4: 3

2 1 4 3 2 1 4 3 2 1 4 3
for 1: remove 1, add 1
1 = 2
for 2: remove 1, remove 1, remove 2, add 1
2 = 2 + 3
for 3: remove 1, remove 1, remove 2, remove 1, remove 3, add 1

n = 4
1 = 2
2 = 2 + (n-2+1) = 2 + 3 = 5 = 1
3 = 1 + (n-3+1) = 1 + 2 = 3


5
1: 2
2: 5
3: 1
4: 2
5: 3
'''


def calc(n):
    if n == 1:
        print('1')
        return
    arr = [0 for _ in range(0, n)]
    arr[1] = 2
    for i in range(2, n+1):
        arr[i] = (arr[i-1] + i) % 4


for _ in range(tc):
    res = calc(int(input()))

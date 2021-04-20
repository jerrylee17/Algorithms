import itertools
def solve(arr):
    cost = 0
    for i in range(len(arr) - 1):
        m = max(arr) + 1
        j = 0
        for x in range(i, len(arr)):
            if arr[x] < m:
                m = arr[x]
                j = x
        cost += j-i+1
        arr = arr[:i] + arr[i:j+1][::-1] + arr[j+1:]
    return cost

# x = [p for p in range(1, 8)]
# perms = list(itertools.permutations(x))
# sols = list(map(solve, perms))
# print(sols)
# print(max(sols))

for i in range(int(input())):
    arrSize = int(input())
    arr = list(map(int, input().split()))
    res = solve(arr)
    print(f'Case #{i+1}: {res}')
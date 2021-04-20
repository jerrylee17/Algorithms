import itertools
def reverseCode(arr):
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

def solve(n, c):
    # lower bound: c = n-1
    # upper bound: c = n*(n+1) / 2
    if not n-1 <= c <= n*(n+1) / 2:
        return 'IMPOSSIBLE'
    arr = [i for i in range(1, n+1)]
    perms = list(itertools.permutations(arr))
    for p in perms:
        if reverseCode(p) == c:
            return ' '.join(list(map(str, p)))
    return 'IMPOSSIBLE'

for i in range(int(input())):
    n, c = list(map(int, input().split()))
    res = solve(n, c)
    print(f'Case #{i+1}: {res}')
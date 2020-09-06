n, m = list(map(int, input().split(' ')))
grid = [0 for i in range(n)]

# Generate grid
for i in range(n):
    row = input()
    grid[i] = [int(c) for c in row]

def dfs(grid, pos, path):
    # Base case: position is bottom left or pos already visited
    if path > m*n: return -1
    if pos == 0: return m*n
    if pos == (n-1, m-1): return path
    # Set current to 0
    tmp = grid[pos[0]][pos[1]]
    grid[pos[0]][pos[1]] = 0
    left, right, bottom, top = pos[1] - tmp, pos[1] + tmp, pos[0] - tmp, pos[0] + tmp
    print(top, n, pos, grid, path)
    if top < n: top = dfs(grid, (top, pos[1]), path+1)
    if bottom >= 0: bottom = dfs(grid, (bottom, pos[1]), path+1)
    if left >= 0: left = dfs(grid, (pos[0], left), path+1)
    if right < m: right = dfs(grid, (pos[0], right), path+1)
    return min(top, bottom, left, right)

# Temporary grid
tmp = [x for x in grid]
result = dfs(tmp,(0,0), 1) or -1
print(result)

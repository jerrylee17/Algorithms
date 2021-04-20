def solve(board):
    curr = board[0][0]
    # target: len(board), len(board[0])
    def traverse(visited, point, currLargest):
        if point[0] == len(board) - 1 and point[1] == len(board[0]) - 1:
            return currLargest
        currHeight = board[point[0]][point[1]]
        directions = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0)
        ]
        largestuff = []
        print(point)
        for d in directions:
            nextPoint = (point[0] + d[0], point[1] + d[1])
            if 0 <= nextPoint[0] < len(board) and 0 <= nextPoint[1] < len(board[0]) and nextPoint not in visited:
                nextLargest = max(currLargest, board[nextPoint[0]][nextPoint[1]] - currHeight)
                largestuff.append(traverse(visited + [nextPoint], nextPoint, nextLargest))
        if len(largestuff):
            currLargest = min(largestuff)
        return currLargest
    largest = traverse([(0,0)], (0, 0), 0)
    return largest




m, n = list(map(int, input().split()))
board = []
for i in range(m):
    board.append(list(map(int, input().split())))

print(solve(board))



def solution(m):
    def generateMap(x, y, m):
        board = [[None for i in range(len(m[0]))] for j in range(len(m))]
        queue = [(x, y)]
        board[x][y] = 1
        while queue:
            # Current square
            square = queue.pop(0)
            squareVal = board[square[0]][square[1]]
            # Squares to move to
            squareArray = [
                (square[0] - 1, square[1]),
                (square[0], square[1] - 1),
                (square[0], square[1] + 1),
                (square[0] + 1, square[1]),
            ]
            # Iterate through the square array
            for s in squareArray:
                # Outside boundaries
                if s[0] < 0 or s[0] >= len(m) or s[1] < 0 or s[1] >= len(m[0]):
                    continue
                # Set the value of the next square
                if not board[s[0]][s[1]]:
                    board[s[0]][s[1]] = squareVal + 1
                    # Movable
                    if m[s[0]][s[1]] == 0:
                        queue.append((s[0], s[1]))
        return board
    forward = generateMap(0, 0, m)
    backward = generateMap(len(m) - 1, len(m[0]) - 1, m)
    smallest = 4000
    for i, r in enumerate(m):
        for j, e in enumerate(r):
            if forward[i][j] and backward[i][j]:
                moves = forward[i][j] + backward[i][j] - 1
                if moves < smallest:
                    smallest = moves
    return smallest


# def solution(m):
#     def test(m):
#         queue = [(0, 0, 1)]
#         spaces = set([])
#         while queue:
#             # Current square
#             square = queue.pop(0)
#             # Add to moved spaces
#             spaces.add((square[0], square[1]))
#             # Destination arrived
#             if square[0] == len(m) - 1 and square[1] == len(m[0]) - 1:
#                 return square[2]
#             # Squares to move to
#             squareArray = [
#                 (square[0] - 1, square[1]),
#                 (square[0], square[1] - 1),
#                 (square[0], square[1] + 1),
#                 (square[0] + 1, square[1]),
#             ]
#             # Iterate through the square array
#             for s in squareArray:
#                 # If already moved
#                 if (s[0], s[1]) in spaces:
#                     continue
#                 # Outside boundaries
#                 if s[0] < 0 or s[0] >= len(m) or s[1] < 0 or s[1] >= len(m[0]):
#                     continue
#                 # Movable
#                 if m[s[0]][s[1]] == 0:
#                     queue.append((s[0], s[1], square[2] + 1))
#         return -1
#     smallest = test(m)
#    for i, r in enumerate(m):
#        for j, e in enumerate(r):
#             # Smallest possible distance reached
#             if smallest == len(m) + len(m[0]) - 1:
#                 return smallest
#             if e == 0:
#                 continue
#             newMat = [r[:] for r in m]
#             newMat[i][j] = 0
#             moves = test(newMat)
#             # moves is possible
#             if moves != -1:
#                 if smallest == -1 or moves < smallest:
#                     smallest = moves
#     return smallest


# t = [[1 for i in range(20)] for j in range(20)]
# t[0] = [0 for i in range(20)]
# t[2] = [0 for i in range(20)]
# t[1][1] = 0
# for i in range(20):
#     t[i][19] = 0
# s = solution(t)
# print(s)
s = solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
print(s)
s = solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [
             0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
print(s)
'''
0 1 1 0
0 0 0 1
1 1 0 0
1 1 1 0

0 0 0 0 0 0
1 1 1 1 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 1 1 1 1 1
0 0 0 0 0 0
'''

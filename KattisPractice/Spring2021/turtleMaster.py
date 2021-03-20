directions = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}
pos = (7, 0)
d = 0
board = []
for i in range(8):
    board.append(input())
poop = input()

for c in poop:
    if c == 'F':
        pos = (pos[0] + directions[d][0], pos[1] + directions[d][1])
        try:
            if board[pos[0]][pos[1]] not in ['.', 'D']:
                print('Bug!')
                break
        except:
            print('Bug!')
            break
    elif c == 'R':
        d = (d + 1) % 4
    elif c == 'L':
        d = (d - 1) % 4
    else:
        np = (pos[0] + directions[d][0], pos[1] + directions[d][1])
        if board[np[0]][np[1]] != 'I':
            print('Bug!')
            break
        else:
            board[np[0]] = board[np[0]][:np[1]] + '.' + board[np[0]][np[1] + 1:]
else:
    if board[pos[0]][pos[1]] == 'D':
        print('Diamond!')
    else:
        print('Bug!')


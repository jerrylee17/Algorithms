tc = int(input())

def win(board, player):
    for i in range(3):
        # Rows
        if ''.join(board[i]) == player*3:
            return True
        # Columns
        if ''.join([a[i] for a in board]) == player*3:
            return True
    # Diagonals
    diagonal1 = ''.join([board[0][0], board[1][1], board[2][2]])
    diagonal2 = ''.join([board[0][2], board[1][1], board[2][0]])
    if diagonal1 == player*3 or diagonal2 == player*3:
        return True
    return False

# count(X) and count(O) are valid
def requirements(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X': count += 1
            if board[i][j] == 'O': count -= 1
    if count == 0 or count == 1:
        return count
    return -1

def tictactoe(board):
    # Requirements: X == O, X = O + 1
    xoxo = requirements(board)
    if xoxo == -1:
        return 'no'
    if xoxo == 0:
        # X cannot have won
        xWins = win(board, 'X')
        if xWins: return 'no'
        return 'yes'
    if xoxo == 1:
        # O cannot have won
        oWins = win(board, 'O')
        if oWins: return 'no'
        return 'yes'
    return False

# Take input
for i in range(tc):
    board = []
    for j in range(3):
        row = input()
        board.append([c for c in row])
    if i != tc - 1:
        input()
    print(tictactoe(board))

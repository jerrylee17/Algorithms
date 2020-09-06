'''
Strategy:
while start not connected to end:
    add shortest route
start from beginning to end
    ladder = biggest increase
'''

def moveducks(board):
    connected = False
    # List of tuples: (start, end, height)
    path = []
    while not connected:
        connected = isConnected(board, path)


# Grab input
m, n = list(map(int,input().split(' ')))
castle = []
for i in range(m):
    row = list(map(int,input().split(' ')))
    castle.append(row)
moveducks(board)




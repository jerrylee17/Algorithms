n = int(input())
arr = []
for i in range(n):
    row = input()
    row = row.split(' ')
    for j in range(n):
        row[j] = int(row[j])
    arr.append(row)

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.vertices = {}

    def insertVert(self, node, weight):
        self.vertices[node] = weight

#create nodes of graph
#village 1 = allNodes[0], 2 = allNodes[1], etc
allNodes = []
for i in range(n):
    node = GraphNode(i)
    allNodes.append(node)

#create vertices of graph
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i == j:
            continue
        allNodes[i].insertVert(j, arr[i][j])
#for i in range(n):
#    print(allNodes[i].val)
#    print(allNodes[i].vertices)

#search, returns T/F
def findNode(currNode, tarNode, tarValue, start, bc):
    if not start and currNode.vertices[tarNode.val] == tarValue:
        return True
    start = False
    c = set()
    for i in range(n):
        if i in bc:
            continue
        if currNode.vertices[i] < tarValue:
            bc.add(i)
            c.add(i)
    for num in c:
        if findNode(allNodes[num],
                    tarNode,
                    tarValue-currNode.vertices[num],
                    start,
                    bc):
            return True

#findNode
for i in range(n):
    for j in range(i+1, n):
        start = True
        if findNode(allNodes[i], allNodes[j], allNodes[i].vertices[j], start, {i}):
            arr[i][j] = 0

for i in range(n):
    for j in range(i+1, n):
        if arr[i][j] != 0:
            print(i+1, j+1)
















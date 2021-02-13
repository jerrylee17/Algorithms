import math
tc = int(input())

class TreeNode:
    def __init__(self, val, level):
        if val == 0:
            self.val = {}
        else:
            self.val = {val: 1}
        self.level = level
        self.left = None
        self.right = None
        self.dale = False

players = []
dale = int(input())
for _ in range(tc - 1):
    p = int(input())
    players.append(p)
# Strongest to weakest
players.sort(reverse=True)
levels = math.floor(math.log2(len(players) + 1))
extras = (len(players) + 1) % (2**levels)

def populateTree(root, levels, extras, players, dale):
    queue = [root]
    while queue:
        currNode = queue[0]
        l = currNode.level
        # Made correct number of levels
        if l == levels:
            break
        # Make left and right nodes and append to queue
        left = TreeNode(0, l+1)
        right = TreeNode(0, l+1)
        currNode.left = left
        currNode.right = right
        queue.append(left)
        queue.append(right)
        # pop the element we just added children to
        queue.pop(0)
    # Spawn extra leaf nodes
    for i in range(extras):
        currNode = queue[0]
        l = currNode.level
        left = TreeNode(0, l+1)
        right = TreeNode(0, l+1)
        currNode.left = left
        currNode.right = right
        queue.append(left)
        queue.append(right)
        queue.pop(0)
    queue = queue[-extras*2:] + queue[:-extras*2]
    # Debug statement
    if len(queue) != len(players) + 1:
        print('BAD TREE CREATION')
        return
    # Populate leaf nodes with correct values
    for i, e in enumerate(players):
        node = queue[i]
        node.val = {e: 1}
    # Last node is dale
    queue[-1].val = {dale: 1}
    queue[-1].dale = True
    # Return leaf nodes
    return queue

def solveTree(root):
    # Leaf node
    if not root.left or not root.right:
        return root
    left = solveTree(root.left)
    right = solveTree(root.right)
    if left.dale or right.dale:
        root.dale = True
        if left.dale:
            dv, dp = list(left.val.items())[0]
            tot = 0
            for v, p in right.val.items():
                tot += p * dv / (dv+v)
            tot *= dp
            root.val = {dv:tot}
        elif right.dale:
            dv, dp = list(right.val.items())[0]
            tot = 0
            for v, p in left.val.items():
                tot += p * dv / (dv+v)
            tot *= dp
            root.val = {dv:tot}
        return root
    for v1, p1 in left.val.items():
        for v2, p2 in right.val.items():
            root.val[v1] = root.val.get(v1, 0) + (v1 / (v1+v2)) * p1 * p2
            root.val[v2] = root.val.get(v2, 0) + (v2 / (v1+v2)) * p1 * p2
    return root

# Champion
root = TreeNode(0, 0)
leafs = populateTree(root, levels, extras, players, dale)
root = solveTree(root)
print(list(root.val.values())[0])

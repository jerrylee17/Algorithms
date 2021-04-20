class node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.failure = None


words = []
for i in range(int(input())):
    words.append(input())
s = input()

root = node('')
def addWord(root, word):
    for child in root.children:
        if child.val == word[0]:
            addWord(child, word[1:])
            break
    else:
        newNode = node(word[0])
        root.children.append(newNode)
        addWord(root.children[-1], word[1:])
            


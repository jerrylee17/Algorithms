# import math
# # import sys
# # sys.setrecursionlimit(3005)


# class TrieNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []
#         self.end = False


# '''
# If you go up a layer and the node is end --> double
# Node value = factorial(children.size)*children.perms
# '''


# def addWord(root, word):
#     if len(word) == 0:
#         root.end = True
#         return
#     for child in root.children:
#         if child.value == word[0]:
#             addWord(child, word[1:])
#             break
#     else:
#         newNode = TrieNode(word[0])
#         root.children.append(newNode)
#         addWord(root.children[-1], word[1:])


# def factorial(n):
#     res = 1
#     for i in range(1, n+1):
#         res = (res * i) % 1_000_000_007
#     return res


# # Post order traversal of children
# def traverse(root):
#     perm = math.factorial(len(root.children) +
#                           int(root.end == True)) % 1_000_000_007
#     for c in root.children:
#         childVal = traverse(c)
#         perm = (perm * childVal) % 1_000_000_007
#     return perm % 1_000_000_007


# n = int(input())
# root = TrieNode(' ')
# for _ in range(n):
#     name = input()
#     addWord(root, name)

# print(traverse(root))

def determineStuff(names):
    letters = 1
    perm = 1
    for i, e in enumerate(names[:-1]):
        pass


n = int(input())
names = []
for _ in range(n):
    name = input()
    names.append(name)

names.sort()
determineStuff(names)

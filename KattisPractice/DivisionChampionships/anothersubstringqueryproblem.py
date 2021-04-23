s = input()
queries = int(input())

for i in range(queries):
    subs, number = input().split()
    index = 0
    count = 0
    currPos = -1
    for j in range(len(s) - len(subs)):
        if s[j:j + len(subs)] == subs:
            count += 1
        if count == int(number):
            currPos = j + 1
            break
    print(currPos)

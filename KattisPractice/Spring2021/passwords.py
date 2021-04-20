'''
36 total chars per slot
A + B
total = 36**b - 36**(a-1)

corner case: xdhaha and hahaxd
'''
reducer = 1_000_003

simDict = {
    'o': 0,
    'i': 1,
    'e': 3,
    's': 5,
    't': 7
}
simList = ['o', 'i', 'e', 's', 't']

a, b = list(map(int, input().split()))

def getVal(x : str):
    specCount = sum([x.count(tmp) for tmp in simList])
    multiplier = 2**specCount
    l = len(x)
    lowerBound = max(a - len(x), 0)
    upperBound = max(b - len(x), 0)
    '''
    math:
    0: 1
    1: 36 * 2
    '''
    


n = int(input())
bl = ['leet']
for i in range(n):
    s = input()
    bl.append(s)



tc = int(input())

def getWord(patterns):
    s = patterns[0]
    for p in patterns[1:]:
        if not fittable(s, p):
            return '*'
        s = combine(s, p)
    return s

def fittable(a, b):
    inda, indb = 0, 0
    while True:
        if a[inda] != '*' and a[inda] == b[indb]:
            inda += 1
            indb += 1
        elif a[inda] == '*':
            inda += 1
            if inda > len(a): return True
            indb = b.find(a[inda], indb)
            # Can't find
            if indb < 0: return False
        elif b[indb] == '*':
            indb += 1
            if indb > len(b): return True
            inda = a.find(b[indb], inda)
            if inda < 0: return False
        else: return False
        if inda >= len(a) or indb >= len(b): return True
    return True

def combine(a, b):
    inda, indb = 0, 0
    s = ''
    while True:
        if a[inda] == '*' and b[indb] == '*':
            s += '*'
            inda += 1
            indb += 1
        elif a[inda] == '*':
            nextwild = b.find('*', indb)
            s += b[indb:nextwild+1]
            indb = nextwild
            inda += 1
            
        elif b[indb] == '*':
            nextwild = b.find('*', inda)
            s += b[inda:nextwild+1]
            inda = nextwild
            indb += 1
        else:
            s += a[inda]
            inda += 1
            indb += 1
        if inda < 0 or indb < 0 or inda >= len(a) or indb >= len(b):
            return s            
    return s

for i in range(tc):
    numPatterns = int(input())
    patterns = []
    for j in range(numPatterns):
        patterns.append(input())
    newstr = getWord(patterns)
    print(newstr)
    
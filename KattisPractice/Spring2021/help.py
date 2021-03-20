import re
tc = int(input())

def solve(s1, s2):
    if len(s1) != len(s2):
        print('-')
        return
    regTest = lambda x: re.match('^<\w*>$', x)
    w1 = {}
    w2 = {}
    uncertainInd = set()
    res = []
    # Get all the forced patterns
    for i, (a, b) in enumerate(zip(s1, s2)):
        # both patterns
        if regTest(a) and regTest(b):
            # Get stuff inside brackets
            res.append(a[1:2])
            uncertainInd.add(i)
        # a is pattern, b isn't
        elif regTest(a) and not regTest(b):
            res.append(b)
            # Not determined yet
            if a not in w1:
                w1[a] = b
            else:
                if w1[a] != b:
                    print('-')
                    return
        # b is pattern, a isn't
        elif not regTest(a) and regTest(b):
            res.append(a)
            # Not determined yet
            if b not in w2:
                w2[b] = a
            else:
                if w2[b] != a:
                    print('-')
                    return
        # Both not patterns
        else:
            res.append(a)
            if a != b:
                print('-')
                return
    while True:
        stillBad = set()
        # Fill uncertain indexes
        for i in uncertainInd:
            # UncertainIndex mapped
            si1 = w1.get(s1[i], '')
            si2 = w2.get(s2[i], '')
            # They match and it works
            if si1 == si2 != '':
                res[i] = si1
            # si2 exists
            elif si1 == '' and si2 != '':
                res[i] = si2
                w1[s1[i]] = si2
            # si1 exists
            elif si1 != '' and si2 == '':
                res[i] = si1
                w2[s2[i]] = si1
            # Both still don't exist
            else:
                if (si1 != '' and si2 != '' and si1 != si2):
                    print('-')
                    return
                stillBad.add(i)
        # Got rid of all the bad stuff
        if not stillBad:
            print(' '.join(res))
            return
        # Nothing changed
        if len(uncertainInd) == len(stillBad):
            break
        uncertainInd = stillBad
    # Solve the rest of the unknowns
    for s in stillBad:
        res[s] = 'xd'

    print(' '.join(res))
            

for _ in range(tc):
    s1 = input().split()
    s2 = input().split()
    solve(s1, s2)

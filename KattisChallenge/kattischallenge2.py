#n(n+1)/2
def testCheck(c):
    tot, count = 1, 0
    c -= 1
    while c > 0:
        c -= tot
        tot += 1
        count += 1
    return count


while True:
    c = int(input())
    if c == 0: break
    print(testCheck(c))
    

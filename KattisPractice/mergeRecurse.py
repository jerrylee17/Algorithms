def recurseMerge(s):
    if len(s) == 1:
        return s
    m = len(s)//2
    return merge(recurseMerge(s[:m]), recurseMerge(s[m:]))

def merge(a, b):
    c = []
    while a or b:
        try:
            if a[0]<b[0]:
                c.append(a[0])
                a.pop(0)
            else:
                c.append(b[0])
                b.pop(0)
        except:
            break
    if a:
        while a:
            c.append(a[0])
            a.pop(0)
    elif b:
        while b:
            c.append(b[0])
            b.pop(0)
    return c

def iterMerge(s):
    l,r = 0, len(s)
    while (l != r):
        

print(recurseMerge([4,2,5,6,1]))

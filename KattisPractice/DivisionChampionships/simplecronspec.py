# total1 = 0
# total2 = 0
# happened = set()

# hour*3600 + min*60 + s
def gen_times(h,m,s, timeSet):
    # Hour
    if h == '*':
        h = set(range(24))
    # Minute
    if m == '*':
        m = set(range(60))
    # Second
    if s == '*':
        s = set(range(60))
    for x in h:
        for y in m:
            for z in s:
                val = x*3600+y*60+z
                timeSet.add(val)


def get_time(a):
    if a == '*':
        return '*'
    res = set()
    times = a.split(',')
    for t in times:
        if len(t.split('-')) == 2:
            lower, higher = list(map(int, t.split('-')))
            res |= set(range(lower, higher+1))
        else:
            res.add(int(t))
    return res

t1, t2 = 0, 0
day = set()
ch, cm, cs = set(), set(), set()
for i in range(int(input())):
    subt = 1
    h, m, s = list(map(get_time, input().split()))
    
    # step 1: divide 24 by hours -> if multiple hours create an array of hours
    # step 2: multiple each hours by 60 and then divide by number of minutes
    # step 3: multiply each minutes by 60 and then divide by each seconds
    # get length of final array

    # Hour
    if h == '*':
        subt *= 24
    else:
        # ch |= h
        subt *= len(h)
    # Minute
    if m == '*':
        subt *= 60
    else:
        subt *= len(m)
        # cm |= m
    # Second
    if s == '*':
        subt *= 60
    else:
        # cs |= cs
        subt *= len(s)
    t2 += subt
    gen_times(h, m, s, day)

print(len(day))
print(t2)
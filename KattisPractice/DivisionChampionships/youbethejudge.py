import sys
import math
# import io, os

def is_prime(n):
    if n <= 1:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True
    
def validNumber(n):
    for x in n:
        if not 48 <= ord(x) <= 57:
            return False
    return True

def checkBounds(x):
    if 3 < x <= 10**9 and x % 2 == 0:
        return True
    else:
        return False

def solve(a):
    # Underscore
    for x in a:
        if not validNumber(x):
            return 0
    # Leading 0's
    if a[0][0] == '0' or a[1][0] == '0' or a[2][0] == '0':
        return 0
    # Valid integers
    try:
        x,y,z = list(map(int, a))
    except:
        return 0

    # negatives
    if x < 0 or y < 0 or z < 0:
        return 0
    if x > y and x > z:
        # if checkBounds(x) and x == y + z and primes(y, z):
        if checkBounds(x) and x == y + z and is_prime(y) and is_prime(z):
            return 1
        return 0
    return 0



res = -1
words = sys.stdin
stuff = []
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# Get 3 tokens
for line in sys.stdin:
    if len(line.strip('\n').split(' ')) == 0:
        continue
    if len(line.strip('\n').split(' ')) > 0:
        lilstuff = line.strip('\n').strip(' ').split()
        stuff.extend(lilstuff)
    if len(stuff) > 3: 
        # This don't work
        res = 0
        break
# Less than 3 tokens
if len(stuff) != 3:
    res = 0
# Over 3 tokens
if res == 0:
    print(0)
else:
    # Process the numbers
    res = solve(stuff)
    print(res)

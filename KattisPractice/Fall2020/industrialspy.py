import math
import itertools
tc = int(input())


def checkIfPrime(x):
    for i in range(2, int(math.sqrt(x)) + 5):
        if x != i and x % i == 0:
            return False
    return True


for _ in range(tc):
    num = input()
    count = 0
    # Check if divisible by 3
    # if sum([int(c) for c in num]) % 3 == 0:
    #     if num == '3':
    #         print(1)
    #         continue
    #     print(count)
    #     continue
    # Check all permutations
    permutations = []
    for i in range(len(num)):
        p = list(itertools.permutations(num, r=(i+1)))
        permutations.extend([int(''.join(x)) for x in p])
        permutations = list(set(permutations))
    for p in permutations:
        if p <= 1:
            continue
        if checkIfPrime(p):
            count += 1
    print(count)

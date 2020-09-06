import sys
import math

'''
0: 3
1: 9*0.5=4.5
2: 4.5+3*0.75=6.75
3: 10.125
4: 15.1875
5: 22.78125
Formula: math.ceil(math.log(3*1.5**n), 10)
But out of bounds error at 10000
'''


def perimeter(n):
    if n == 0: return 1
    return math.ceil(math.log(3, 10)+n*math.log(1.5, 10))


for i, line in enumerate(sys.stdin):
    decimals = perimeter(int(line))
    print(f'Case {i + 1}: {decimals}')




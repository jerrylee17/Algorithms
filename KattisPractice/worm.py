import math
x = input()
x = x.split(' ')
(climb, fall, target) = [int(e) for e in x]

days = ((target - climb)/(climb - fall)) + 1

if target <= climb:
    days = 1
if target == 0:
    days = 0

print(math.ceil(days))

import re
a, b = input().split(' ')

name = a

if a[-1] == 'e':
    name += 'x' + b
elif re.match('[aiou]', name[-1]):
    name = name[:-1] + 'ex' + b
elif re.match('(ex)', name[-2:]):
    name += b
else:
    name += 'ex' + b

print(name)

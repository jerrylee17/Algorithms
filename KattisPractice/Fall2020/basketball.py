s = input()

a, b = 0, 0

for i, c in enumerate(s[::2]):
    score = s[2*i+1]
    if c == 'A':
        a += int(score)
    elif c == 'B':
        b += int(score)

if a > b:
    print('A')
else:
    print('B')

while True:
    x = input()
    (num, den) = x.split(' ')
    num, den = int(num), int(den)
    if num == 0 or den == 0:
        break
    s = ''
    s += str(num//den) + ' '
    s += str(num % den) + ' / ' + str(den)
    print(s)

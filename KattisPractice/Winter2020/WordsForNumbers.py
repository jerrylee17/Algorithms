import sys


def solve(line):
    numberMap = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }
    res = ''
    for word in line.split(' '):
        try:
            number = int(word)
            if number <= 20 or number % 10 == 0:
                res += numberMap[number] + ' '
            else:
                tens = (number//10) * 10
                ones = number % 10
                res += f'{numberMap[tens]}-{numberMap[ones]}' + ' '
        except:
            res += word + ' '
    # Make first thingy upper
    res = res[0].upper() + res[1:]
    print(res)
    return


for line in sys.stdin:
    solve(line)

# https://open.kattis.com/problems/aliennumbers

tc = int(input())

def convertToBase(digits, currBase, targetBase):
    num = 0
    count = 0
    # Convert to base 10
    for digit in digits[::-1]:
        num += digit * (currBase**count)
        count += 1

    result = []
    # Convert to target base
    while num:
        result = [int(num % targetBase)] + result
        num //= targetBase
    return result

for i in range(tc):
    number, src, target = input().split(' ')
    digits = []
    # convert number to base 10 digits in an array (HUMAN werds)
    for x in number:
        digits.append(src.find(x))
    # convert the digits into a target base and return an array
    newDigits = convertToBase(digits, len(src), len(target))
    # convert human readable numbers to alien numbers
    for index, digit in enumerate(newDigits):
        newDigits[index] = target[digit]
    # join the converted numbers
    result = ''.join(newDigits)
    print(f'Case #{i+1}: {result}')


"""
20 to base 2 10100

20 / 2 = 10 mod 0
10 / 2 = 5 mod 0
5 / 2 = 2 mod 1
2 / 2 = 1 mod 0
1 / 2 = 0 mod 1

"""

# from math import ceil

# print(10 ** 9 - 1)


def H(previousHash, transaction, target):
    v = previousHash
    token = 0

    for i in range(len(transaction)):
        v = (v*31 + ord(transaction[i])) % 1000000007

    # for i in range(999999999):
    #    c_v = (v * 7 + i) % 1000000007
    #    if c_v % 10000000 == 0:
    #        token = i
    #        break
    token = v + round(v * 7, -7) % 999999999

    # print("v, token:", v, token)
    # (A + X) % B = C
    # C = hash
    # A = v * 7
    # X = token
    # B = 1000000007
    # (B + C - A) % B = X
    token = (1000000007 + target - v * 7) % 1000000007
    # print(v * 7, v)
    return ((v * 7 + token) % 1000000007, token)


prev = int(input())
word_one, word_two = "d", "d"  # 218216710

target, target2 = 930000000, 730000000
a = H(prev, word_one, target)
b = H(a[0], word_two, target2)

# print(word_one + " " + str(a[0]) + "Token: " + str(a[1]))
# print(word_two + " " + str(b[0]) + "Token: " + str(b[1]))
print(word_one + " " + str(a[1]))
print(word_two + " " + str(b[1]))
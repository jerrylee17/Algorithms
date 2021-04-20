import math

x = int(input())
l = 0
r = 250000
while True:
    m = (l + r) // 2
    f = math.factorial(m)
    if x > f:
        l = m + 1
    elif x == f:
        print(m)
        break
    else:
        r = m - 1



# p = 0
# for c in x[::-1]:
#     if c == '0':
#         p += 1
#     else:
#         break
# count = p * 5
# while p > 1:
#     p //= 5
#     count -= p * 5
# x = int(x) / math.factorial(count)
# while x >= 1:
#     count += 1
#     x /= count
# print(count - 1)

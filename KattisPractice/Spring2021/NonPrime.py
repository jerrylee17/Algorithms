from math import sqrt
import io, os, sys


def getFac(num):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 
    953, 967, 971, 977, 983, 991, 997]
    count = 0
    f = 1
    c = 0
    # test 2
    while num % 2 == 0:
        count += 1
        num //= 2
    if count != 0:
        f *= count + 1
        c += 1
    if num == 1:
        return f - 1
    for p in primes:
        if p > int(sqrt(num)):
            break
        count = 0
        while num % p == 0:
            count += 1
            num //= p
        if count != 0:
            f *= count + 1
            c += 1
        if num == 1:
            break
    if num > 1:
        f *= 2
        c += 1
    return f - c

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
for i in range(int(float(input().decode()))):
    num = int(float(input().decode()))
# for i in range(int(input())):
#     num = int(input())
    facs = getFac(num)

    sys.stdout.write(f'{facs}\n')

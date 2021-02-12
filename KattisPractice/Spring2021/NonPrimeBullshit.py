from math import sqrt
def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def genPrime():
    primes = [2, 3]
    for i in range(4, 1_000):
        if isPrime(i):
            primes.append(i)
    return primes

p = genPrime()
print(p)


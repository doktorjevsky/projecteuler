from problem7 import sieve

"""
Find the sum of all the primes below two million.
"""

PRIMES = [2]
n = 1000
while PRIMES[-1] < 2 * (10 ** 6):
    PRIMES = sieve(n)
    n *= 2

s = 0
for i in range(len(PRIMES)):
    if PRIMES[i] >= 2 * (10 ** 6):
        break
    else:
        s += PRIMES[i]

print(s)


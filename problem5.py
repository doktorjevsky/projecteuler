
"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


PRIMES      = [2, 3, 5, 7, 11, 13, 17, 19]
PRIME_COUNT = [0, 0, 0, 0, 0,  0,  0,  0 ]

prod = 1

for i in range(1, 21):
    for j in range(len(PRIME_COUNT)):
        k = 0
        while i % PRIMES[j] == 0:
            k += 1
            i //= PRIMES[j]
        if k > PRIME_COUNT[j]:
            PRIME_COUNT[j] = k


for z in zip(PRIMES, PRIME_COUNT):
    prod *= z[0] ** z[1]

print(prod)




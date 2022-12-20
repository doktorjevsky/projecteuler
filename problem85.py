import math

from problem7 import sieve


"""
How many numbers below 50 * 10^6 can be expressed as

a^2 + b^3 + c^4, where a, b, c are primes=
"""


def main():
    X = 50 * 1_000_000
    upper_bound = int((X - 24) ** 0.5)
    PRIMES = sieve(upper_bound)
    place1 = []
    place2 = []
    place3 = []
    for p in PRIMES:
        if p**2 + 2**3 + 2**4 < X:
            place1.append(p)
        if 2**2 + p**3 + 2**4 < X:
            place2.append(p)
        if 2**2 + 2**3 + p**4 < X:
            place3.append(p)

    c = set()
    for p3 in place3:
        for p2 in place2:
            for p1 in place1:
                n = p1 ** 2 + p2 ** 3 + p3 ** 4
                if n < X:
                    c.add(n)

    print(len(c))



if __name__ == '__main__':
    main()
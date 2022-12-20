
"""
What is the 10 001st prime number?
"""

def sieve(n):
    bools = list(True for _ in range(n+1))
    primes = []
    for i in range(2, len(bools)):
        if bools[i]:
            primes.append(i)
            for j in range(2*i, len(bools), i):
                bools[j] = False
    return primes



def main():
    PRIMES = sieve(11 * 10000)
    print(PRIMES[10000])
    print(sieve(100))

if __name__ == '__main__':
    main()


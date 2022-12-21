from problem7 import sieve
import heapq


def simulate(a, b, prime_set):
    f = lambda n: n * n + a * n + b
    n = 0
    while prime_set.__contains__(f(n)):
        n += 1
    return n

def main():
    PRIMES = sieve(1000)
    prime_set = set(PRIMES)

    sign = (1, -1)
    q = []
    for a in PRIMES:
        for i in sign:
            for b in PRIMES:
                for j in sign:
                    n = simulate(a*i, b*j, prime_set)
                    heapq.heappush(q, (-n, (a*i, b*j)))
    res = heapq.heappop(q)
    print(res[1][0] * res[1][1])



if __name__ == '__main__':
    main()
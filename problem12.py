import math

"""
first triangular number to have over 500 divisors
"""

def n_divisors(n):
    stop = int(math.sqrt(n)) + 1
    divs = set()
    for i in range(1, stop):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return len(divs)


def main():
    f = lambda x: x*(x+1) // 2
    n = 1
    number = f(n)
    while n_divisors(number) <= 500:
        n += 1
        number = f(n)
    print(number)

if __name__ == '__main__':
    main()
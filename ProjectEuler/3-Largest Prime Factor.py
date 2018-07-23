'''
23/07/2018
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt
n = 600851475143
limit = int(sqrt(n))

def get_primes(start, end):
    '''
    Getting all prime numbers with use Sieve of Eratosthenes algorithm
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    '''
    dct = {x: True for x in list(range(start, end+1))}
    x = start

    while x ** 2 <= end:
        if dct[x]:
            y = x ** 2
            while y <= end:
                dct[y] = False
                y += x
        x += 1

    result = []
    for x, y in dct.items():
        if y:
            result.append(x)

    return result


primes = get_primes(2, limit)

divisors = list(filter(lambda x: n % x == 0, primes))

print(max(divisors))

#Answer: 6857

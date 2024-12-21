# https://www.hackerrank.com/contests/projecteuler/challenges/euler007/
import sys

def primeN(primes, n):
    curr = primes[-1]+2
    while len(primes) < n:
        prime = True
        for i in primes:
            if i*i > curr:
                break
            if curr % i == 0:
                prime = False
                break
        if prime:
            primes.append(curr)
        curr += 2
    return primes[n-1]

primes = [2, 3]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primeN(primes, n))

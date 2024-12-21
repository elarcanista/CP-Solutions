# https://www.hackerrank.com/contests/projecteuler/challenges/euler041/
import itertools as iter
import math

def sieve(N):
    prime = [True] * math.ceil(math.sqrt(N))
    prime[0] = prime[1] = False
    primes = []
    p = 2
    while p**2 <= N:
        if prime[p]:
            primes.append(p)
            for kp in range(2*p, len(prime), p):
                prime[kp] = False
        p += 1
    return prime, primes
    
def is_prime(N, prime, primes):
    if N <= primes[-1]:
        return prime[N]
    for p in primes:
        if N % p == 0:
            return False
        if p**2 > N:
            break
    return True

def get_panprimes(prime, primes):
    pans = [-1]
    for d in range(1, 10):
        for p in iter.permutations(range(1, d+1)):
            num = int(concat(p))
            if is_prime(num, prime, primes):
                pans.append(num)
    return sorted(pans)

def concat(p):
    ans = ""
    for c in p:
        ans += str(c)
    return ans

def bsearch(S, n):
    left = 0
    right = len(S)-1
    while left != right:
        mid = math.ceil((left+right)/2)
        if S[mid] == n:
            return mid
        if S[mid] < n:
            left = mid
        else:
            right = mid - 1
    return left

max_N = 10**10 - 1
prime, primes = sieve(max_N)
panprimes = get_panprimes(prime, primes)
panprimes[0] = -1

for _ in range(int(input())):
    N = int(input())
    print(panprimes[bsearch(panprimes, N)])

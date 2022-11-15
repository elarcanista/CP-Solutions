import math

def sieve(N):
    prime = [True] * (N+1)
    prime[0] = prime[1] = False
    primes = []
    p = 2
    while p**2 <= N:
        if prime[p]:
            primes.append(p)
            for kp in range(2*p, N+1, p):
                prime[kp] = False
        p += 1
    while p <= N:
        if prime[p]:
            primes.append(p)
        p += 1
    return prime, primes

def goldbach(N, primes):
    ans = 0
    for p in primes:
        if p >= N:
            break
        square = (N - p)/2
        square_sqrt = math.sqrt(square)
        if square_sqrt == int(square_sqrt):
            ans += 1
    return ans

max_N = 5*10**5
prime, primes = sieve(max_N)

for _ in range(int(input())):
    N = int(input())
    print(goldbach(N, primes))
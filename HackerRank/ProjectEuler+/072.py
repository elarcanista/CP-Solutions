def sieve(max_n):
    prime = [True] * (max_n + 1)
    prime[0] = prime[1] = False
    primes = []
    i = 2
    while i**2 <= len(prime):
        if prime[i]:
            primes.append(i)
            i_k = 2*i
            while i_k < len(prime):
                prime[i_k] = False
                i_k += i
        i += 1
    return primes

def factorize(n, primes):
    factors = []
    for p in primes:
        if p**2 > n:
            break
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                exponent += 1
                n //= p
            factors.append((p, exponent))
    if len(factors) == 0:
        return [(n, 1)]
    if n != 1:
        factors.append((n, 1))
    return factors

def phi(n, primes):
    acum = 1
    for (p, k) in factorize(n, primes):
        acum *= p**(k - 1) * (p - 1)
    return acum

MAX_N = 10**6
primes = sieve(MAX_N)
ans = [0]

T = int(input())
for _ in range(T):
    N = int(input())
    if len(ans) - 1 < N:
        for n in range(len(ans), N+1):
            ans.append(ans[-1] + phi(n, primes))
    print(ans[N])

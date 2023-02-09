def sieve(N):
    is_prime = [True] * (N+1)
    is_prime[0] = is_prime[1] = False
    primes = []
    p = 2
    while p**2 <= N:
        if is_prime[p]:            
            primes.append(p)
            for kp in range(2*p, N+1, p):
                is_prime[kp] = False
        p += 1
    while p <= N:
        if is_prime[p]:
            primes.append(p)
        p += 1
    return is_prime, primes

def max_primes(a, b, is_prime):
    n = 0
    while is_prime[n**2 + a*n + b]:
        n += 1
    return n

is_prime, primes = sieve(10**6)

N = int(input())

max_params = (1, 41)
max_n = 40
for b in range(2, N+1):
    for a in range(1-b, N+1):
        n = max_primes(a, b, is_prime)
        if n > max_n:
            max_n = n
            max_params = (a, b)

print(*max_params)
def is_prime(N, primes):
    if is_coprime(N, primes):
        return miller(N)
    return False

def is_coprime(N, primes):
    limit = int(N**(1/2)) + 1
    for p in primes:
        if p > limit:
            return True
        if N % p == 0:
            return False
    return True

def sieve(N):
    prime = 3 # 0b11
    primes = [2]
    p = 3
    while p <= N:
        if prime & (1 << p) == 0:
            primes.append(p)
            for kp in range(3*p, N+1, 2*p):
                prime |= 1 << kp
        p += 2
    return primes

miller_range = [2, 3, 5, 7, 11]

def exp(a, b, m): # (a**b) % m
    res = 1
    while b > 1:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a ** 2) % m
        b //= 2
    return (a * res) % m

def miller(n):
    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in miller_range:
        x = exp(a,d,n)
        for _ in range(s):
            y = exp(x,2,n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True

primes = sieve(1000)

N = int(input())
    
corners = 5
curr = 9
corner_primes = 3
side = 3

while (100 * corner_primes) // corners >= N:
    side += 2
    for _ in range(4):
        curr = curr + side - 1
        corners += 1
        if is_prime(curr, primes):
            corner_primes += 1
print(side)
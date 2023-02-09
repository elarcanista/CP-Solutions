def sieve():
    prime = 3
    primes = []
    p = 2
    while len(primes) < 20:
        if prime & (1 << p) == 0:
            primes.append(p)
            for kp in range(2*p, 101, p):
                prime |= (1 << kp)
        p += 1
    return primes

def max_ratio(N):
    n = 1
    for p in primes:
        if n*p >= N:
            break
        n *= p
    return n

primes = sieve()
for _ in range(int(input())):
    N = int(input())
    print(max_ratio(N))

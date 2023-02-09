def sieve(N):
    prime = [True] * (N + 1)
    prime[0] = prime[1] = False
    p = 2
    while p*p <= N:
        if prime[p]:
            for kp in range(2*p, N, p):
                prime[kp] = False
        p += 1
    return prime

def circular(p, prime):
    pwr = len(str(p))
    for _ in range(1, pwr):
        p = (p % 10**(pwr-1))*10 + p // 10**(pwr-1)
        if not prime[p]:
            return False
    return True

max_N = 10**6
prime = sieve(max_N)

N = int(input())

ans = 0
for p in range(N):
    if prime[p] and circular(p, prime):
        ans += p
print(ans)
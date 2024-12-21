# https://www.hackerrank.com/contests/projecteuler/challenges/euler037/
def sieve(N):
    prime = [True] * (N+1)
    prime[0] = prime[1] = False
    p = 2
    while p*p <= N:
        if prime[p]:
            for kp in range(2*p, N, p):
                prime[kp] = False
        p += 1
    return prime

def truncable(N):
    n = N
    while n != 0:
        if not prime[n]:
            return False
        n = n // 10
    mod = 10
    while n != N:
        n = N % mod
        if not prime[n]:
            return False
        mod *= 10
    return True

max_N = 10**6
prime = sieve(max_N)

N = int(input())

ans = 0
for n in range(10, N):
    if truncable(n):
        ans += n
print(ans)

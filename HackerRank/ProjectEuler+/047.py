def sieve(N):
    prime = [0] * (N+1)
    p = 2
    while p*2 <= N:
        if prime[p] == 0:
            for kp in range(p*2, N+1, p):
                prime[kp] += 1
        p += 1
    return prime

def find(N, k, prime):
    acum = 0
    for p in range(N + k):
        if prime[p] == k:
            acum += 1
        else:
            acum = 0
        if acum >= k:
            print(p - k + 1)

max_N = 2*10**6+5
prime = sieve(max_N)
N, K = map(int, input().split())
find(N, K, prime)
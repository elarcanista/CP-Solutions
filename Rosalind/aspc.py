def choose(n, k):
    if n == k or k == 0:
        return 1
    if (n, k) in pascal:
        return pascal[(n, k)]
    pascal[(n, k)] = (choose(n-1, k-1) + choose(n-1, k)) % 1000000
    return pascal[(n, k)]

pascal = {}
n, m = map(int, input().split())

ans = 0

for N in range(n):
    for M in range(N+1):
        choose(N, M)
for k in range(m, n+1):
    ans = (ans + choose(n, k)) % 1000000
print(ans)
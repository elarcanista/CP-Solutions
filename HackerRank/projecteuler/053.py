# https://www.hackerrank.com/contests/projecteuler/challenges/euler053/
def choose(n, m):
    ans = 1
    for i in range(m+1, n+1):
        ans *= i
    for i in range(2, n-m+1):
        ans //= i
    return ans

N, K = map(int, input().split())

C = []
ans = 0
for n in range(N+1):
    r = n//2
    if choose(n,r) <= K:
        continue
    for r in range(n+1):
        c = choose(n,r)
        C.append(c)
        if c > K:
            ans += 1
    break

n += 1
while n <= N:
    C2 = [1]
    for i in range(len(C)-1):
        C2.append(C[i] + C[i+1])
        if C2[-1] > K:
            ans += 1
    C2.append(1)
    C = C2
    n += 1

print(ans)

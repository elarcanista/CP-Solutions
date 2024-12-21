# https://www.hackerrank.com/contests/projecteuler/challenges/euler052/
def freq(n):
    S = str(n)
    ans = {}
    for c in S:
        if c in ans:
            ans[c] += 1
        else:
            ans[c] = 1
    return ans

N, K = map(int, input().split())
freq(N)
for n in range(1, N+1):
    s = freq(n)
    good = True
    for k in range(1, K+1):
        if freq(k*n) != s:
            good = False
            break
    if good:
        print(*[k*n for k in range(1, K+1)])

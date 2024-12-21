# https://www.hackerrank.com/contests/projecteuler/challenges/euler055/
def next(N):
    N2 = int(str(N)[::-1])
    return N + N2

def fill(N, it):
    if it >= 60:
        return
    p = next(N)
    if p - N == N:
        if N in count:
            count[N] += 1
        else:
            count[N] = 1
        return
    fill(p, it + 1)

max_N = int(input())
count = {}

for n in range(10, max_N + 1):
    fill(n, 0)
ans = max(count, key=count.get)
print(ans, count[ans])


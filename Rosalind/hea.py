def add(S, n):
    i = len(S)
    S.append(n)
    while i > 1 and n > S[i//2]:
        S[i], S[i//2] = S[i//2], S[i]
        i //= 2

N = int(input())
S = list(map(int, input().split()))
ans = [None]
for s in S:
    add(ans, s)
print(*ans[1:])
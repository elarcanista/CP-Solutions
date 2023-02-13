import math

N, K = map(int, input().split())
S = set(map(int, input().split()))
S_mod = {}
for k in range(K):
    S_mod[k] = 0
for s in S:
    S_mod[s % K] += 1
ans = 0
for k in range(1, math.ceil(K/2)):
    ans += max(S_mod[k], S_mod[K - k])
if S_mod[0] > 0:
    ans += 1
if K % 2 == 0 and S_mod[K//2] > 0:
    ans += 1
print(ans)
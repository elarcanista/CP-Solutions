N = int(input())
S = list(map(int, input().split()))
S2 = {}
for s in S:
    if s not in S2:
        S2[s] = 0
    S2[s] += 1
ans = 0
for v in S2.values():
    ans += v//2
print(ans)
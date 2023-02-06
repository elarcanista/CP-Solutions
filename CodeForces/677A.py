N, H = map(int, input().split())
S = map(int, input().split())
ans = 0
for s in S:
    if s > H:
        ans += 1
    ans += 1
print(ans)
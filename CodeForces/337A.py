w, N = map(int, input().split())
S = sorted(list(map(int, input().split())))

ans = S[-1] - S[0]
for i in range(len(S) - w + 1):
    ans = min(S[i + w - 1] - S[i], ans)
print(ans)
S = []
for _ in range(4):
    S.append(int(input()))
d = [True] * (int(input()) + 1)

ans = 0
for s in S:
    for ns in range(s, len(d), s):
        if d[ns]:
            d[ns] = False
            ans += 1
print(ans)
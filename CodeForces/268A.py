S = []
for _ in range(int(input())):
    S.append(tuple(map(int, input().split())))

ans = 0
for h, _ in S:
    for _, g in S:
        if h == g:
            ans += 1
print(ans)
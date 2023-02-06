ans = 0
for _ in range(int(input())):
    p, q = map(int, input().split())
    if p+2 <= q:
        ans += 1
print(ans)
a, b, k = map(int, input().split())
ans = 0
for n in range(a, b+1):
    if abs(n - int(str(n)[::-1])) % k == 0:
        ans += 1

print(ans)
a, b = map(int, input().split())

ans = 0
for n in range(a, b+1):
    if n % 2 == 1:
        ans += n
print(ans)
N = int(input())

ans = 0
for n in [100, 20, 10, 5, 1]:
    ans += N // n
    N %= n

print(ans)
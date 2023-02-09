mod = 10**10
ans = 0

N = int(input())
for i in range(1, N+1):
    ans += pow(i,i, mod) % mod
print(ans % mod)
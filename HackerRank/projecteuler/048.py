# https://www.hackerrank.com/contests/projecteuler/challenges/euler048/
mod = 10**10
ans = 0

N = int(input())
for i in range(1, N+1):
    ans += pow(i,i, mod) % mod
print(ans % mod)

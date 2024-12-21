# https://www.hackerrank.com/contests/projecteuler/challenges/euler031/
max_N = 10**5
mod = 10**9 + 7
mem = [1] * (max_N + 1)
coins = [2, 5, 10, 20, 50, 100, 200]

for c in coins:
    for i in range(max_N + 1):
        if c <= i:
            mem[i] = (mem[i] + mem[i - c]) % mod

for _ in range(int(input())):
    N = int(input())
    print(mem[N])

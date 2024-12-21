# https://www.hackerrank.com/contests/projecteuler/challenges/euler028/
mod = 10**9 + 7
for _ in range(int(input())):
    L = int(input()) // 2
    print((2*(1 + L*(13 + 15*L + 8*L**2)//3) - 1) % mod)

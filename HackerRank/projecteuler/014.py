# https://www.hackerrank.com/contests/projecteuler/challenges/euler014/
hue = []

def collatz(N, length):
    if N < len(length):
        if length[N] != 0:
            return length[N]
    if N % 2 == 0:
        next = N//2
    else:
        next = 3*N + 1
    ans = collatz(next, length) + 1
    if N < len(length):
        length[N] = ans
    return ans


max_N = 5 * 10**6
length = [0] * (max_N + 1)
length[1] = 1
greatest = [0] * (max_N + 1)

for n in range(1, max_N + 1):
    temp = collatz(n, length)
    if temp >= length[greatest[n-1]]:
        greatest[n] = n
    else:
        greatest[n] = greatest[n-1]

for _ in range(int(input())):
    N = int(input())
    print(greatest[N])

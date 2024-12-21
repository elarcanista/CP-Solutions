# https://www.hackerrank.com/contests/projecteuler/challenges/euler024/
def fact(N):
    ans = 1
    for i in range(2,N+1):
        ans *= i
    return ans

def permutation(N, str):
    if len(str) <= 1:
        return str
    total = fact(len(str) - 1)
    pos = N // total
    return str[pos] + permutation(N % total, str[:pos] + str[pos+1:])

for _ in range(int(input())):
    N = int(input())
    print(permutation(N-1, "abcdefghijklm"))

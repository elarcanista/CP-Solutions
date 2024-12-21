# https://www.hackerrank.com/contests/projecteuler/challenges/euler043/
import itertools as iter

primes = [2,3,5,7,11,13,17]

def get_pans(N):
    ans = 0
    for t in iter.permutations(range(N+1)):
        s = "".join(map(str, t))
        divisible = True
        for i in range(1, len(s)-2):
            if int(s[i:i+3]) % primes[i-1] != 0:
                divisible = False
                break
        if divisible:
            ans += int(s)
    return ans

N = int(input())
print(get_pans(N))

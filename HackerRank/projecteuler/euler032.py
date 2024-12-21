# https://www.hackerrank.com/contests/projecteuler/challenges/euler032/
from math import *

def merge(a, b, c):
    return str(a) + str(b) + str(c)

def pandigital(num, N):
    digits = set(map(int, list(num)))
    return len(num) == len(digits) and digits == set(range(1, N+1))

N = int(input())
prods = set()
ans = 0

for n in range(int(10**ceil(N/2))):
    S = str(n)
    if len(set(S)) != len(S):
        continue
    for j in range(1, len(S)):
        a, b = S[:j], S[j:]
        c = str(int(a)*int(b))
        if pandigital(a + b + c, N):
            prods.add(int(c))
print(sum(prods))

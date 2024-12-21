# https://www.hackerrank.com/challenges/magic-square-forming/
import itertools as iter

def magic(m):
    H = sum(m[0:3]) == 15 and sum(m[3:6]) == 15 and sum(m[6:9]) == 15
    V = sum(m[0::3]) == 15 and sum(m[1::3]) == 15 and sum(m[2::3]) == 15
    D = m[0] + m[4] + m[8] == 15 and m[2] + m[4] + m[6] == 15
    return H and V and D

def cost(A, B):
    ans = 0
    for a, b in zip(A, B):
        ans += abs(a - b)
    return ans

A = list(map(int, input().split()))
A += list(map(int, input().split()))
A += list(map(int, input().split()))

ans = 9*9
for B in iter.permutations(range(1, 10)):
    if magic(B):
        ans = min(ans, cost(A, B))

print(ans)

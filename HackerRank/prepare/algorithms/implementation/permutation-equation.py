# https://www.hackerrank.com/challenges/permutation-equation/
N = int(input())
L = list(map(int, input().split()))
L2 = list(map(lambda x: L.index(x) + 1, range(1, N+1)))
L2 = list(map(lambda x: L.index(x) + 1, L2))
print(*L2, sep="\n")

# https://www.hackerrank.com/challenges/the-hurdle-race/
N, k = map(int, input().split())
S = max(map(int, input().split()))

print(max(S-k, 0))

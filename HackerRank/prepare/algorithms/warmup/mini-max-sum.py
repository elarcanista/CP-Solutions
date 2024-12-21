# https://www.hackerrank.com/challenges/mini-max-sum/
S = list(map(int, input().split()))
print(sum(S) - max(S), sum(S) - min(S))

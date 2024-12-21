# https://www.hackerrank.com/challenges/birthday-cake-candles/
N = int(input())
S = list(map(int, input().split()))
ans = 0
max_S = max(S)
for s in S:
    if s == max_S:
        ans += 1
print(ans)

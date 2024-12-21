# https://www.hackerrank.com/challenges/staircase/
N = int(input())
ans = ""
for i in range(1, N):
    ans += " "
ans += "#"
for i in range(N):
    print(ans)
    ans = ans[1:] + "#"

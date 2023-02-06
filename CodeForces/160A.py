N = int(input())
S = sorted(map(int, input().split()), reverse=True)
brother = sum(S)
me = 0
ans = 0
for s in S:
    if me > brother:
        break
    brother -= s
    me += s
    ans += 1
print(ans)
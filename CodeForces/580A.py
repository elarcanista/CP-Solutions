N = int(input())
S = list(map(int, input().split()))
last = 0
ans = 0
curr = 0
for s in S:
    if s >= last:
        curr += 1
        ans = max(curr, ans)
    else:
        curr = 1
    last = s
print(ans)
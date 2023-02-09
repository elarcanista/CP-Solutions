N = int(input())
S = list(map(int, input().split()))
sum_S, lenght_S = map(int, input().split())

ans = 0
curr = sum(S[:lenght_S])
if curr == sum_S:
    ans += 1
for i in range(lenght_S, len(S)):
    curr -= S[i-lenght_S]
    curr += S[i]
    if curr == sum_S:
        ans += 1
print(ans)
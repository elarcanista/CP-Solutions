N = int(input())
S = list(map(int, input().split()))
checked = set()

ans = 0
for i, s1 in enumerate(S):
    curr = 0
    if s1 in checked:
        continue
    checked.add(s1)
    for s2 in S[i:]:
        if s2 - s1 in [0, 1]:
            curr += 1
    ans = max(curr, ans)
    
    curr = 0
    for s2 in S[i:]:
        if s1 - s2 in [0, 1]:
            curr += 1
    ans = max(curr, ans)
print(ans)
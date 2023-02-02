N = int(input())
S = list(map(int, input().split()))
S2 = {S[0]: 1}
max_S = S[0]
ans = 0
for i in range(1, len(S)):
    copy = S[i]
    base = 1
    pair = 0
    while copy != 1:
        if copy % 2:
            copy += 1
            pair += base
        copy >>= 1
        base *= 2
    while pair <= max_S:
        if pair in S2:
            ans += S2[pair]
        pair += base
        base *= 2
    if S[i] not in S2:
        S2[S[i]] = 0
    S2[S[i]] += 1
    max_S = max(S[i], max_S)
print(ans)
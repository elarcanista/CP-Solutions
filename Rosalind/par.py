N = int(input())
S = list(map(int, input().split()))
i = 0
j = 1
while j < len(S):
    if i < j and S[i] >= S[j]:
        S[i], S[j] = S[j], S[i]
        i, j = j, i
    if i > j and S[i] < S[j]:
        S[i], S[j] = S[j], S[i]
        i, j = j, i
    j += 1
print(*S)
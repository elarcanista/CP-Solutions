N = int(input())
S = list(map(int, input().split()))
l = r = 0
j = 1
while j < len(S):
    if j < l and S[j] > S[r]:
        S[r], S[j] = S[j], S[r]
        S[j], S[l-1] = S[l-1], S[j]
        l -= 1
        r -= 1
        continue
    elif j > r and S[j] < S[l]:
        S[l], S[j] = S[j], S[l]
        S[j], S[r+1] = S[r+1], S[j]
        l += 1
        r += 1
        continue
    elif j < l and S[j] == S[l]:
        S[l-1], S[j] = S[j], S[l-1]
        l -= 1
        continue
    elif j > r and S[j] == S[r]:
        S[r+1], S[j] = S[j], S[r+1]
        r += 1
        continue
    j += 1
print(*S)
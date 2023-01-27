def sort(S, l, r):
    def merge(L, R):
        ans = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                ans.append(L[i])
                i += 1
            else:
                ans.append(R[j])
                j += 1
        if j >= len(R):
            ans += L[i:]
        else:
            ans += R[j:]
        return ans

    if l == r:
        return [S[l]]
    m = (l + r) // 2
    L = sort(S, l, m)
    R = sort(S, m+1, r)
    
    return merge(L, R)

N = int(input())
S = list(map(int, input().split()))

print(*sort(S, 0, len(S) - 1))
def sort(S):
    def merge(L, R):
        ans = []
        invs = 0
        i=j=0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                ans.append(R[j])
                invs += len(L) - i
                j += 1
            else:
                ans.append(L[i])
                i += 1
        while i < len(L):
            ans.append(L[i])
            i += 1
        while j < len(R):
            ans.append(R[j])
            j += 1
        return ans, invs
    if len(S) == 1:
        return S, 0
    m = len(S)//2
    L, L_inv = sort(S[:m])
    R, R_inv = sort(S[m:])
    ans, invs = merge(L, R)
    return ans, L_inv + R_inv + invs

N = int(input())
S = list(map(int, input().split()))
print(sort(S)[1])
import sys

def lcsq(A, B):
    memo = {}

    def suff(i, j):
        if (i,j) in memo:
            return memo[(i, j)]
        if i < 0 or j < 0:
            return ""
        if A[i] == B[j]:
            ans = suff(i-1, j-1) + A[i]
        else:
            C = suff(i-1, j)
            D = suff(i, j-1)
            if len(C) > len(D):
                ans = C
            else:
                ans = D
        memo[(i,j)] = ans
        return ans
    
    ans = ""
    for i in range(len(A)):
        for j in range(len(B)):
            curr = suff(i, j)
            if len(curr) > len(ans):
                ans = curr
    return ans

A = input()
B = input()
C = lcsq(A, B)
ans = ""
for c in C:
    while A[0] != c:
        ans += A[0]
        A = A[1:]
    while B[0] != c:
        ans += B[0]
        B = B[1:]
    ans += c
    A = A[1:]
    B = B[1:]
while A != "":
    ans += A[0]
    A = A[1:]
while B != "":
    ans += B[0]
    B = B[1:]
print(ans)
import sys

def read_input():
    FASTA = []
    input()
    current_DNA = ""
    for line in sys.stdin:
        if line[0] == ">":
            FASTA.append(current_DNA)
            current_DNA = ""
        else:
            current_DNA += line.strip()
    FASTA.append(current_DNA)
    return FASTA

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

A, B = read_input()
print(lcsq(A, B))

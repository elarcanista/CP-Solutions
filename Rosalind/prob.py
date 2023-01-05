import math

DNA = input()
CG = list(map(float, input().split()))

def prob_nucleotide(CG):
    return {
        "A": (1 - CG)/2,
        "C": CG/2,
        "G": CG/2,
        "T": (1 - CG)/2,
    }

def prob_string(CG):
    P = prob_nucleotide(CG)
    ans = 0
    for c in DNA:
        ans += math.log10(P[c])
    return ans

print(*[round(prob_string(cg), 3) for cg in CG])

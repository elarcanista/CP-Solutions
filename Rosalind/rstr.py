N, CG = map(float, input().split())
DNA = input()

p_nucleotide = {"A": (1-CG)/2, "C": CG/2, "G": CG/2, "T": (1-CG)/2}

p_str = 1

for c in DNA:
    p_str *= p_nucleotide[c]

print(1-(1-p_str)**N)
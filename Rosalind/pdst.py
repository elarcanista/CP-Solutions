import sys

def read_input():
    input()
    FASTA = []
    current_DNA = ""
    for line in sys.stdin:
        if line[0] == ">":
            FASTA.append(current_DNA)
            current_DNA = ""
        else:
            current_DNA += line.strip()
    FASTA.append(current_DNA)
    return FASTA

def pdist(A, B):
    ans = 0
    for cA, cB in zip(A, B):
        if cA != cB:
            ans += 1
    return ans / len(A)

FASTA = read_input()
D = [[0]*len(FASTA) for _ in FASTA]

for i in range(len(FASTA)):
    for j in range(i+1, len(FASTA)):
        d = pdist(FASTA[i], FASTA[j])
        D[i][j] = D[j][i] = d

for d in D:
    print(*d)
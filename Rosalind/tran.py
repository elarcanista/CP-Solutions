import sys

def read_FASTA():
    FASTA = []
    curr_name = input()[1:].strip()
    curr_DNA = input()

    for line in sys.stdin:
        line = line.strip()
        if line[0] == ">":
            FASTA.append(curr_DNA)
            curr_DNA = ""
        else:
            curr_DNA += line

    FASTA.append(curr_DNA)
    return FASTA

FASTA = read_FASTA()

transition = {"A": "G", "C": "T", "G": "A", "T": "C"}

T1 = 0
T2 = 0
for i in range(len(FASTA[0])):
    if transition[FASTA[0][i]] == FASTA[1][i]:
        T1 += 1
    elif FASTA[0][i] != FASTA[1][i]:
        T2 += 1

print(T1 / T2)
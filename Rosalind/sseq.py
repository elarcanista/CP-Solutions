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

j = 0

for i, c in enumerate(FASTA[0]):
    if c == FASTA[1][j]:
        print(i+1, end=" ")
        j += 1
    if j >= len(FASTA[1]):
        break

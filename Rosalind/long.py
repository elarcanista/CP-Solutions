import sys

def read_FASTA():
    FASTA = {}
    curr_name = input()[1:].strip()
    curr_DNA = input()

    for line in sys.stdin:
        line = line.strip()
        if line[0] == ">":
            FASTA[curr_name] = curr_DNA
            curr_name = line[1:]
            curr_DNA = ""
        else:
            curr_DNA += line

    FASTA[curr_name] = curr_DNA
    return list(FASTA.values())

FASTA = read_FASTA()

def overlap(X, Y):
    max = -1
    for i in range(min(len(X), len(Y))):
        if X[-i:] == Y[:i]:
            max = i
    return max

def get_best():
    best = (-1, -1, -1)
    for i in range(len(FASTA)):
        for j in range(len(FASTA)):
            if i == j:
                continue
            curr = overlap(FASTA[i], FASTA[j])
            if curr > best[0]:
                best = (curr, i, j)
    return best

while len(FASTA) > 1:
    best = get_best()
    FASTA[best[1]] += FASTA[best[2]][best[0]:]
    FASTA.pop(best[2])

print(FASTA[0])
import sys
import math

def read_input():
    FASTA = {}

    current_name = input()[1:]
    current_DNA = input()

    for line in sys.stdin:
        line = line.strip()
        if line[0] == ">":
            FASTA[current_name] = current_DNA
            current_name = line[1:]
            current_DNA = ""
        else:
            current_DNA += line
    FASTA[current_name] = current_DNA
    return list(FASTA.values())

def lcsstr(Xs):
    shortest = Xs[0]
    for x in Xs:
        if len(x) < len(shortest):
            shortest = x
    Ys = []
    for x in Xs:
        if x != shortest:
            Ys.append(x)
    best = ""
    for start in range(len(shortest)):
        for end in range(start + 1, len(shortest) + 1):
            if len(shortest[start:end]) <= len(best):
                continue
            good = True
            for x in Ys:
                if shortest[start:end] not in x:
                    good = False
                    break
            if good:
                best = shortest[start:end]
    return best

print(lcsstr(read_input()))
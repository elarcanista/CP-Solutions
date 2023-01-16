import sys

def read_input():
    input()
    current_DNA = ""
    for line in sys.stdin:
        current_DNA += line.strip()
    return current_DNA

def preprocess(DNA):
    lpp = [0] * len(DNA)
    curr = 0
    i = 1
    while i < len(DNA):
        if DNA[i] == DNA[curr]:
            curr += 1
            lpp[i] = curr
            i += 1
        elif curr != 0:
            curr = lpp[curr-1]
        else:
            lpp[i] = 0
            i += 1
    return lpp

DNA = read_input()

print(*preprocess(DNA))
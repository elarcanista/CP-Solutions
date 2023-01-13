import sys

def read_input():
    input()
    current_DNA = ""
    for line in sys.stdin:
        current_DNA += line.strip()
    return current_DNA

DNA = read_input()
A, C, G, U = map(DNA.count, ["A", "C", "G", "U"])
matchings = 1
while A != 0 and U != 0:
    matchings *= max(A, U)
    A -= 1
    U -= 1
while C != 0 and G != 0:
    matchings *= max(C, G)
    C -= 1
    G -= 1

print(matchings)
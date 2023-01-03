import sys
pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}

def reverse(s):
    sc = ""
    for nt in reversed(s):
        sc += pairs[nt]
    return sc

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
    return list(FASTA.values())[0]

s = read_input()
for start in range(len(s)):
    for end in range(start+4, len(s)+1):
        if end-start <= 12 and s[start:end] == reverse(s[start:end]):
            print(start + 1, end-start)

import sys

def rc(DNA):
    pair = {"A": "T", "C": "G", "G": "C", "T": "A"}
    DNA_rc = ""
    for nucleotide in reversed(DNA):
        DNA_rc += pair[nucleotide]
    return DNA_rc

S = set()
for line in sys.stdin:
    S.add(line.strip())
    S.add(rc(line.strip()))

B = {}

for s in S:
    if s[:-1] in B: 
        B[s[:-1]].add(s[1:])
    else:
        B[s[:-1]] = {s[1:]}

for u in B:
    for v in B[u]:
        print(f"({u}, {v})")
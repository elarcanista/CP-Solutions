import sys

table = {
    "TTT": "F",      "CTT": "L",      "ATT": "I",      "GTT": "V",
    "TTC": "F",      "CTC": "L",      "ATC": "I",      "GTC": "V",
    "TTA": "L",      "CTA": "L",      "ATA": "I",      "GTA": "V",
    "TTG": "L",      "CTG": "L",      "ATG": "M",      "GTG": "V",
    "TCT": "S",      "CCT": "P",      "ACT": "T",      "GCT": "A",
    "TCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "TCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "TCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "TAT": "Y",      "CAT": "H",      "AAT": "N",      "GAT": "D",
    "TAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "TAA": "$",      "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "TAG": "$",      "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "TGT": "C",      "CGT": "R",      "AGT": "S",      "GGT": "G",
    "TGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "TGA": "$",      "CGA": "R",      "AGA": "R",      "GGA": "G",
    "TGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}

def rc(DNA):
    DNAc = ""
    for nt in reversed(DNA):
        DNAc += pairs[nt]
    return DNAc

def frames(DNA):
    prot = [""]*6
    for start in range(3):
        for i in range(start, len(DNA) - 2, 3):
            prot[start] += table[DNA[i:i+3]]
    
    DNA = rc(DNA)
    for start in range(3):
        for i in range(start, len(DNA) - 2, 3):
            prot[start + 3] += table[DNA[i:i+3]]

    return prot

def read_frame(prot):
    start = []
    ans = set()
    for i, P in enumerate(prot):
        if P == "M":
            start.append(i)
        if P == "$":
            for s in start:
                ans.add(prot[s:i])
            start = []
    return ans

gene = ""
input()
for line in sys.stdin:
    gene += line.strip()

ans = set()
for f in frames(gene):
    ans = ans.union(read_frame(f))
for a in ans:
    print(a)
print()

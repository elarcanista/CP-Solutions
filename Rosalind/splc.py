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
    "TAA": "",      "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "TAG": "",      "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "TGT": "C",      "CGT": "R",      "AGT": "S",      "GGT": "G",
    "TGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "TGA": "",      "CGA": "R",      "AGA": "R",      "GGA": "G",
    "TGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

def reading():
    input()
    DNA = ""
    for line in sys.stdin:
        if line[0] == ">":
            break
        else:
            DNA += line.strip()
    introns = set()
    current_DNA = ""
    for line in sys.stdin:
        if line[0] == ">":
            introns.add(current_DNA)
            current_DNA = ""
        else:
            current_DNA += line.strip()
    introns.add(current_DNA)
    return DNA, introns

def read_frame(DNA):
    prot = ""
    for i in range(0, len(DNA) - 2, 3):
        prot += table[DNA[i:i+3]]
    return prot

DNA, introns = reading()

for i in introns:
    start = DNA.find(i)
    while start != -1:
        DNA = DNA[:start] + DNA[start + len(i):]
        start = DNA.find(i)
print(read_frame(DNA))
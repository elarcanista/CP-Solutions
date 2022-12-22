import sys

def reading():
    FASTA = {}
    current_name = input()[1:].strip()
    current_DNA = ""
    for line in sys.stdin:
        if line[0] == ">":
            FASTA[current_name] = current_DNA
            current_name = line[1:].strip()
            current_DNA = ""
        else:
            current_DNA += line.strip()
    FASTA[current_name] = current_DNA
    return FASTA

FASTA = reading()
best = ("", 0)
for name, DNA in FASTA.items():
    GC = (DNA.count("G") + DNA.count("C")) / len(DNA)
    if GC > best[1]:
        best = (name, GC)
print(best[0])
print(f"{best[1]:%}"[:-1])

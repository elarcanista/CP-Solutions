import sys

start = {}

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

for name, DNA in FASTA.items():
    if DNA[:3] not in start:
        start[DNA[:3]] = [name]
    else:
        start[DNA[:3]].append(name)

for name, DNA in FASTA.items():
    if DNA[-3:] not in start:
        continue
    for name2 in start[DNA[-3:]]:
        if name2 != name:
            print(name, name2)
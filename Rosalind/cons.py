import sys

nucleotides = ["A", "C", "G", "T"]
curr_name = ""
FASTA = {}
for line in sys.stdin:
    line = line.strip()
    if line[0] == ">":
        curr_name = line[1:]
        FASTA[curr_name] = ""
    else:
        FASTA[curr_name] += line
    
length = len(list(FASTA.values())[0])
profile = dict(zip(nucleotides,
    [[0]*length, [0]*length, [0]*length, [0]*length]))
for gene in FASTA.values():
    for i, N in enumerate(gene):
        profile[N][i] += 1

consensus = ""
for i in range(length):
    max_value = max(map(lambda N: profile[N][i], nucleotides))
    for N in nucleotides:
      if profile[N][i] == max_value:
        consensus += N
        break
print(consensus)
for N in nucleotides:
    print(f"{N}:", *profile[N])
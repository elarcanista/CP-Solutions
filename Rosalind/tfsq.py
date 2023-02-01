import sys
from Bio import SeqIO
from textwrap import wrap

s = [line for line in sys.stdin]
with open(".in", "w") as file:
    file.writelines(s)
with open(".in", "r") as file:
    records = SeqIO.parse(file, "fastq")
    for r in records:
        print(">", r.id, sep="")
        for line in wrap(str(r.seq), 70):
            print(line)
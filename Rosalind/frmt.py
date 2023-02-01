from Bio import Entrez
from Bio import SeqIO
from textwrap import wrap

id = input().split()
Entrez.email = "aortega0703@gmail.com"
handle = Entrez.efetch(
    db="nucleotide", 
    id=id, 
    rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
ans = min(records, key=lambda x: len(x.seq))
print(">", ans.description, sep="")
for l in wrap(str(ans.seq), 70):
    print(l)
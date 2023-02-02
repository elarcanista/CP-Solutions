from Bio import Entrez
import subprocess
import re

id = input().split()
Entrez.email = "aortega0703@gmail.com"
handle = Entrez.efetch(
    db="nucleotide", 
    id=id, 
    rettype="fasta")
FASTA = handle.read().split("\n\n")
with open(".in", "w") as file:
    file.write(FASTA[0])
cmd = [
    "needle",
    "-bsequence", ".in",
    "-datafile", "EDNAFULL",
    "-gapopen", "10.0",
    "-gapextend", "1.0",
    "-endweight",
    "-endopen", "10.0",
    "-endextend", "1.0",
    "-aformat3", "pair",
    "-filter"
]
p = subprocess.run(cmd, input=FASTA[1], capture_output=True, text=True).stdout
ans = re.findall("Score: (-?\d+)(?:\.\d+)?", p)
print(ans[0])
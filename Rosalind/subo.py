import subprocess
import Bio.SeqIO
import sys
import re

def dist(A, B):
    distance = 0
    for a, b in zip(A, B):
        if a != b:
            distance += 1
    return distance

def count(seq, match, hamm):
    ans = 0
    for i in range(len(seq) - len(match)):
        if dist(seq[i: i + len(match)], match) <= hamm:
            ans += 1
    return ans

S = [line for line in sys.stdin]
with open(".in", "w") as file_in:
    file_in.writelines(S)
with open(".in", "r") as file_in:
    records = Bio.SeqIO.parse(file_in, "fasta")
    seqs = []
    for r in records:
        seqs.append(str(r.seq))
with open(".in", "w") as file_in:
    file_in.writelines(">test\n" + seqs[0])
command = [
    "lalign36",
    "-n",
    "-q",
    "@",
    ".in"
]
out = subprocess.run(command, input=">test\n" + seqs[1], capture_output=True, text=True).stdout.splitlines()
regex = re.compile("100\.0\% identity \(100\.0\% similar\) in (\d+)")
for i, line in enumerate(out):
    match = regex.match(line)
    if match is not None and int(match.group(1)) >= 32 and int(match.group(1)) <= 40:
        match = out[i+3][7:]
        break
print(count(seqs[0], match, 3), count(seqs[1], match, 3))
        
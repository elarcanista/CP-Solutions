import sys
import subprocess
import Bio.SeqIO

S = [line for line in sys.stdin]
with open(".in", "w") as file_in:
    file_in.writelines(S)
cmd = [
    "getorf",
    "-sequence", ".in", ".out"
]
p = subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines()
with open(".out", "r") as file_in:
    records = Bio.SeqIO.parse(file_in, "fasta")
    ans = ""
    for r in records:
        r = str(r.seq)
        try:
            r = r[r.index("M"):]
            if len(r) > len(ans):
                ans = r
        except:
            pass
    print(ans)
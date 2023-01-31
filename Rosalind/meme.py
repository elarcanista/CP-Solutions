import sys
import subprocess

input_file = ".in"
s = [line for line in sys.stdin]
with open(input_file, "w") as FASTA:
    FASTA.writelines(s)
cmd = f"meme {input_file} -text -minw 20 -nmotifs 1"
output = subprocess.getoutput(cmd).splitlines()
for i, line in enumerate(output):
    if "regular expression" in line:
        print(output[i+2])
        break

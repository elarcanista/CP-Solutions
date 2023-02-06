import subprocess
import sys

S = [line for line in sys.stdin]
with open(".in", "w") as file_in:
    file_in.writelines(S)

cmd = [
    "clustalw",
    ".in"
]

subprocess.run(cmd, capture_output=True)

with open(".aln", "r") as file_in:
    print(file_in.read().splitlines()[-2].split()[0])
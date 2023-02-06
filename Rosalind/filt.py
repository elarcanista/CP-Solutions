import subprocess
import sys

q, p = map(int, input().split())
S = [line for line in sys.stdin]
with open(".in", "w") as file_in:
    file_in.writelines(S)
cmd = [
    "./fastq_quality_filter",
    "-q", str(q),
    "-p", str(p),
    "-Q33",
    "-i", ".in"
]
p = subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines()
print(len(p)//4)
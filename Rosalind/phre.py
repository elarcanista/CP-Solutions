import Bio.SeqIO
import sys

threshold = int(input())
S = [line for line in sys.stdin]
with open(".in", "w") as file_in:
    file_in.writelines(S)
ans = 0
with open(".in", "r") as file_in:
    records = Bio.SeqIO.parse(file_in, "fastq")
    for r in records:
        quality = r.letter_annotations["phred_quality"]
        if sum(quality)/len(quality) < threshold:
            ans += 1
print(ans)
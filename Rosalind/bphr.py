import sys
import Bio.SeqIO

N = int(input())
lines = [line for line in sys.stdin]
with open(".in", "w") as file_in:
    file_in.writelines(lines)
ans = 0
with open(".in", "r") as file_in:
    records = Bio.SeqIO.parse(file_in, "fastq")
    quality = []
    for r in records:
        quality.append(r.letter_annotations["phred_quality"])
    for i in range(len(quality[0])):
        average = 0
        for j in range(len(quality)):
            average += quality[j][i]
        average /= len(quality)
        if average < N:
            ans += 1
print(ans)
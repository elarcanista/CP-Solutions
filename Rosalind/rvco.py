import Bio.SeqIO
import sys

text = [line for line in sys.stdin]
with open(".in", "w") as file_in:
    file_in.writelines(text)
with open(".in", "r") as file_in:
    records = Bio.SeqIO.parse(file_in, "fasta")
    ans = 0
    for r in records:
        if r.seq == r.seq.reverse_complement():
            ans += 1
print(ans)
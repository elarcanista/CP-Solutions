import sys
import Bio.SeqIO
import Bio.SeqRecord
import Bio.Seq

N = int(input())
lines = [line for line in sys.stdin]
with open(".in", "w") as file_in:
    file_in.writelines(lines)

with open(".in", "r") as file_in:
    records = list(Bio.SeqIO.parse(file_in, "fastq"))

sequences = []
for r in records:
    quality = r.letter_annotations["phred_quality"]
    sequence = str(r.seq)
    for i, q in enumerate(quality):
        if q >= N:
            break
    quality = quality[i:]
    sequence = sequence[i:]
    for i, q in reversed(list(enumerate(quality))):
        if q >= N:
            break
    quality = quality[:i+1]
    sequence = sequence[:i+1]
    
    sequences.append((r.id, sequence, quality))

for i, (id, seq, q) in enumerate(sequences):
    seq = Bio.Seq.Seq(seq)
    sequences[i] = Bio.SeqRecord.SeqRecord(seq=seq, id=id, letter_annotations={"phred_quality": q})


with open(".out", "w") as file_out:
    Bio.SeqIO.write(sequences, file_out, "fastq")

with open(".out", "r") as file_out:
    print(file_out.read())
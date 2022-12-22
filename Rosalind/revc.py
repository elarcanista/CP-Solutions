pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}

s = input()
sc = ""

for nt in reversed(s):
    sc += pairs[nt]

print(sc)
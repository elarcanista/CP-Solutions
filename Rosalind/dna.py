DNA = input()
nt = {}
for c in DNA:
    if c not in nt:
        nt[c] = 0
    nt[c] += 1

print(nt['A'], nt['C'], nt['G'], nt['T'])
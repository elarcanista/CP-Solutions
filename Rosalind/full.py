import sys

mass = {
    "A":   71.03711,
    "C":   103.00919,
    "D":   115.02694,
    "E":   129.04259,
    "F":   147.06841,
    "G":   57.02146,
    "H":   137.05891,
    "I":   113.08406,
    "K":   128.09496,
    "L":   113.08406,
    "M":   131.04049,
    "N":   114.04293,
    "P":   97.05276,
    "Q":   128.05858,
    "R":   156.10111,
    "S":   87.03203,
    "T":   101.04768,
    "V":   99.06841,
    "W":   186.07931,
    "Y":   163.06333
}

parent = float(input())
L = []
G = {}
for line in sys.stdin:
    w = float(line.strip())
    L.append(w)
    G[w] = []

L = sorted(L, reverse=True)
pairs = []

n = (len(L) - 2)//2
for i, w1 in enumerate(L):
    for w2 in L[i+1:]:
        if abs(parent - (w1 + w2)) < 0.001:
            pairs.append((w1, w2)) 
        for k, m in mass.items():
            if abs(w1 - (w2 + m)) < 0.001:
                G[w2].append((w1, k))

u = L[-1]
for _ in range(n):
    print(G[u][-1][1], end="")
    u = G[u][-1][0]
print()
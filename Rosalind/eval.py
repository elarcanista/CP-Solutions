N = int(input())
DNA = input()
CG = map(float, input().split())

for cg in CG:
    p = 1
    for c in DNA:
        if c in ["C", "G"]:
            p *= cg/2
        else:
            p *= (1-cg)/2

    print((N - len(DNA) + 1) * p, end=" ")
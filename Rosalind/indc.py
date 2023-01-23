import math

N = int(input())

P = []
for k in range(0, 2*N + 1):
    P.append(0)
    for x in range(k, 2*N +1):
        P[-1] += math.comb(2*N, x)
    P[-1] = round(math.log10(P[-1]) + math.log10((1/2)**(2*N)), 4   )
print(*P[1:])

import math

P = {
    3: (lambda n: n*(n + 1)//2,
        lambda n: (1 + math.sqrt(1 + 8*n))/2),
    5: (lambda n: n*(3*n - 1)//2,
        lambda n: (1 + math.sqrt(1 + 24*n))/6),
    6: (lambda n: n*(2*n - 1),
        lambda n: (1 + math.sqrt(1 + 8*n))/4),
}

N, a, b = map(int, input().split())

Pn = n = 1
while Pn < N:
    k = P[a][1](Pn)
    if k == int(k):
        print(Pn)
    n += 1
    Pn = P[b][0](n)

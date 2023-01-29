import math

V, E = map(int, input().split())
G = []
for _ in range(E):
    u, v, w = map(int, input().split())
    G.append((w, u-1, v-1))

E = G
D = [math.inf]*V
D[0] = 0
for _ in range(V-1):
    for w, u, v in E:
        if D[u] + w < D[v]:
            D[v] = D[u] + w
for u in range(V):
    if D[u] == math.inf:
        D[u] = "x"
print(*D)
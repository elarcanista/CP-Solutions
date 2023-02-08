import math

def SPFA():
    D[0] = 0
    stack = [0]
    while stack:
        u = stack[-1]
        for v in G[u]:
            if D[u] + W[(u, v)] < D[v]:
                D[v] = D[u] + W[(u, v)]
                stack.append(v)
                break
        else:
            stack.pop()


V, E = map(int, input().split())
G = [[] for _ in range(V)]
W = {}
D = [math.inf] * V
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u-1].append(v-1)
    W[(u-1, v-1)] = w
SPFA()
for i in range(len(D)):
    if D[i] == math.inf:
        D[i] = "x"
print(*D)
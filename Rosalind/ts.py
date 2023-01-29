def DFS(u):
    if visited[u]:
        return
    visited[u] = True
    for v in G[u]:
        DFS(v)
    topo.append(u + 1)

V, E = map(int, input().split())
G = [[] for _ in range(V)]
D = [0] * V
for _ in range(E):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    D[v-1] += 1

visited = [False] * V
topo = []
for u in range(V):
    if D[u] == 0:
        DFS(u)
print(*topo[::-1])
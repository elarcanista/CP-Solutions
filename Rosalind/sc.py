def kosaraju(G, G2):
    def DFS(G, u, c = None):
        if visited[u]:
            return
        visited[u] = True if c is None else c
        for v in G[u]:
            DFS(G, v, c)
        if c is None:
            stack.append(u)

    visited = [False] * len(G)
    stack = []
    for u in range(len(G)):
        DFS(G, u)
    visited = [False] * len(G)
    c = 1
    while len(stack) > 0:
        u = stack.pop()
        if not visited[u]:
            DFS(G2, u, c)
            c += 1
    for u in range(len(G)):
        visited[u] -= 1
    return visited

def toposort(u):
    if visited[u]:
        return
    visited[u] = True
    for v in G3[u]:
        toposort(v)
    topo.append(u)

ans = []
for _ in range(int(input())):
    input()
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    G2 = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G2[v-1].append(u-1)
    C = kosaraju(G, G2)
    E = set()
    G3 = [[] for _ in range(max(C) + 1)]
    for u in range(V):
        for v in G[u]:
            if C[u] != C[v] and (C[u], C[v]) not in E:
                E.add((C[u], C[v]))
                G3[C[u]].append(C[v])
    visited = [False] * len(G3)
    topo = []
    for u in range(len(G3)):
        toposort(u)
    topo = topo[::-1]
    for i in range(len(G3) - 1):
        if (topo[i], topo[i+1]) not in E:
            ans.append(-1)
            break
    else:
        ans.append(1)
print(*ans)
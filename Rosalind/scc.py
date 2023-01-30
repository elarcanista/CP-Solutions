def kosaraju(G, G2):
    def DFS(G, u, component = None):
        if visited[u]:
            return 
        visited[u] = True if component is None else component
        for v in G[u]:
            DFS(G, v, component)
        if component is None:
            stack.append(u)

    visited = [False] * len(G)
    stack = []
    for u in range(len(G)):
        DFS(G, u)
    visited = [False] * len(G)
    counter = 0
    while len(stack) > 0:
        u = stack.pop()
        if not visited[u]:
            counter += 1
        DFS(G2, u, counter)
    return counter


V, E = map(int, input().split())

G = [[] for _ in range(V)]
G2 = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G2[v-1].append(u-1)
print(kosaraju(G, G2))
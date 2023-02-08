def index(N):
    if N > 0:
        return (N - 1) * 2
    else:
        return (-N - 1) * 2 + 1

def kosaraju(G, G2, V):    
    # Uses C to store both components and visited status
    def DFS(G, u, c = True):
        stack = [u]
        C[u] = c
        while stack:
            u = stack[-1]
            for v in G[u]:
                if C[v] is None:
                    C[v] = c
                    stack.append(v)
                    break
            else:
                post.append(u)
                stack.pop()
    # Fills post numbers on first DFS pass
    C = [None] * V
    post = []
    for u in range(V):
        if C[u] is None:
            DFS(G, u)
    # Traverses G2 on post order and fills components
    C = [None] * V
    c = 0
    while post:
        u = post.pop()
        if C[u] is None:
            DFS(G2, u, c)
            c += 1
    C2 = [[] for _ in range(c)]
    for i in range(V):
        C2[C[i]].append(i)
    return C, C2, c

for _ in range(int(input())):
    input()
    V, E = map(int, input().split())
    G = [[] for v in range(2*V)]
    G2 = [[] for v in range(2*V)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[index(-u)].append(index(v))
        G[index(-v)].append(index(u))
        G2[index(v)].append(index(-u))
        G2[index(u)].append(index(-v))
    C, C2, c = kosaraju(G, G2, 2*V)
    for u in range(V):
        if C[2*u] == C[2*u+1]:
            print(0)
            break
    else:
        EGC2 = set()
        GC2 = [[] for _ in range(c)]
        ans = [None] * (2*V)
        for u in range(2*V):
            for v in G2[u]:
                if C[u] != C[v] and (C[u], C[v]) not in EGC2:
                    GC2[C[u]].append(C[v])
                    EGC2.add((C[u], C[v]))
        for c in reversed(range(c)):
            value = None
            for u in C2[c]:
                if ans[u] is not None:
                    value = ans[u]
            if value is None:
                value = True
            for u in C2[c]:
                ans[u] = value
                if u % 2 == 0:
                    u += 1
                else:
                    u -= 1
                ans[u] = not value
        ans2 = []
        for i in range(V):
            if ans[2*i]:
                ans2.append(i+1)
            else:
                ans2.append(-(i+1))
        print(1, *ans2)
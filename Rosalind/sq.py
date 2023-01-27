def DFS(u, d):
    if d > 4:
        return 0
    if D[u] != -1:
        if d - D[u] == 4:
            return 1
        else:
            return 0
    D[u] = d
    for v in G[u]:
        if u != v and DFS(v, d+1) == 1:
            return 1
    D[u] = -1
    return 0

for _ in range(int(input())):
    input()
    N, L = map(int, input().split())
    G = [[] for _ in range(N)]
    D = [-1] * N
    for _ in range(L):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    for u in range(N):
        if DFS(u, 0) == 1:
            print(1, end=" ")
            break
    else:
        print(-1, end=" ")
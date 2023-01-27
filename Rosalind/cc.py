def DFS(u):
    vis[u] = True
    for v in G[u]:
        if not vis[v]:
            DFS(v)

N, L = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(L):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

CC = list(range(N))
vis = [False] * N
ans = 0
for u in range(N):
    if not vis[u]:
        ans += 1
        DFS(u)
print(ans)
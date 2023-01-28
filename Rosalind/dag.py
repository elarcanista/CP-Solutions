def DFS(u):
    visited[u] = True
    for v in G[u]:
        if visited[v]:
            return False
        if not DFS(v):
            return False
    visited[u] = False
    return True

ans = []
for _ in range(int(input())):
    input()
    V, L = map(int, input().split())
    G = [[] for _ in range(V)]
    D = [0] * V
    visited = [False]*V
    for _ in range(L):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        D[v-1] += 1
    if D.count(0) == 0:
        ans.append(-1)
        continue
    for u in range(V):
        if D[u] > 0:
            continue
        if not DFS(u):
            ans.append(-1)
            break
    else:
        ans.append(1)
print(*ans)
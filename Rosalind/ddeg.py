N, L = map(int, input().split())

G = [[] for _ in range(N)]
D = [0]*N
DD = [0]*N
for _ in range(L):
    u, v = map(int, input().split())
    D[u-1] += 1
    D[v-1] += 1
    G[u-1].append(v-1)
    G[v-1].append(u-1)

for u in range(N):
    DD[u] = sum(map(lambda x: D[x], G[u]))

print(*DD)
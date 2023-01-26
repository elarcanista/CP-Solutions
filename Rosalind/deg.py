N, M = map(int, input().split())
deg = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    deg[u-1] += 1
    deg[v-1] += 1

print(*deg)
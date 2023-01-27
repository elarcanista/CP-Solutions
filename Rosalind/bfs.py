import queue

def BFS(u):
    q = queue.Queue()
    q.put((0, u))
    while not q.empty() > 0:
        w, u = q.get()
        if D[u] != -1:
            continue
        D[u] = w
        for v in G[u]:
            q.put((w+1, v))

N, L = map(int, input().split())
G = [[] for _ in range(N)]
D = [-1] * N
for _ in range(L):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
BFS(0)
print(*D)
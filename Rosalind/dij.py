import queue
import math

def dijkstra(u):
    q = queue.PriorityQueue()
    q.put((0, u))
    while not q.empty():
        w, u = q.get()
        if w >= D[u]:
            continue
        D[u] = w
        for w, v in G[u]:
            q.put((D[u] + w, v))

V, E = map(int, input().split())
G = [[] for _ in range(V)]
D = [math.inf] * V
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u-1].append((w, v-1))
dijkstra(0)
for i in range(V):
    if D[i] == math.inf:
        D[i] = -1
print(*D)
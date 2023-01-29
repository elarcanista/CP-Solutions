import queue
import math

def dijkstra(source):
    q = queue.PriorityQueue()
    q.put((0, source))
    while not q.empty():
        w, u = q.get()
        if w > D[u]:
            continue
        D[u] = w
        for w, v in G[u]:
            if D[u] + w < D[v]:
                q.put((D[u] + w, v))

ans = []

for _ in range(int(input())):
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    end, source, e_w = map(int, input().split())
    end -= 1
    source -= 1
    G[end].append((e_w, source))
    for _ in range(E - 1):
        u, v, w = map(int, input().split())
        G[u-1].append((w, v-1))
    D = [math.inf] * V
    dijkstra(source)
    if D[end] == math.inf:
        ans.append(-1)
    else:
        ans.append(D[end] + e_w)
print(*ans)
import math
import queue

def SPFA():
    q = queue.Queue()
    L = [0] * V
    for u in range(V):
        D[u] = 0
        q.put(u)
    while not q.empty():
        u = q.get()
        for w, v in G[u]:
            if D[u] + w < D[v]:
                D[v] = D[u] + w
                L[v] = L[u] + 1
                if L[v] == V:
                    return True
                if v not in q.queue:
                    q.put(v)
    return False

ans = []
for _ in range(int(input())):
    # input()
    V, E = map(int, input().split())
    D = [math.inf]*V
    E2 = []
    G = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        E2.append((w, u-1, v-1))
        G[u-1].append((w, v-1))
    E = E2
    if SPFA():
        ans.append(1)
    else:
        ans.append(-1)
print(*ans)
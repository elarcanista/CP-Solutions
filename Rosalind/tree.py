import sys
import queue

def BFS(start):
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        if component[u] != -1:
            continue
        component[u] = start
        for v in G[u]:
            q.put(v)

N = int(input())

G = [[] for _ in range(N)]
for line in sys.stdin:
    u, v = map(int, line.split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

component = [-1] * N
ans = 0

for u in range(N):
    if component[u] == -1:
        BFS(u)
        ans += 1

print(ans - 1)
def DFS(u):
    stack = [(1, u)]
    depth = 0
    while len(stack) > 0:
        d, u = stack.pop()
        depth = max(d, depth)
        for v in G[u]:
            stack.append((d+1, v))
    return depth
    
V = int(input())
G = [[] for _ in range(V)]
D = [0] * V
for u in range(V):
    v = int(input())
    if v != -1:
        G[v-1].append(u)
        D[u] += 1
depth = 0
for u in range(V):
    if D[u] == 0:
        depth = max(depth, DFS(u))
print(depth)

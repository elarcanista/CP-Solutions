def color(u, c):
    C[u] = c
    for v in G[u]:
        if C[v] != None:
            if C[v] == c:
                return False
        elif not color(v, not c):
            return False
    return True

for _ in range(int(input())):
    input()
    V, L = map(int, input().split())
    G = [[] for _ in range(V)]
    C = [None] * V
    for _ in range(L):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    for u in range(V):
        if C[u] == None:
            if not color(u, True):
                print(-1, end = " ")
                break
    else:
        print(1, end= " ")
print()
for _ in range(int(input())):
    input()
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    D = [0] * V
    for _ in range(E):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        D[v-1] += 1

    ans = []
    while D.count(0) == 1:
        u = D.index(0)
        for v in G[u]:
            D[v] -= 1
        D[u] -= 1
        ans.append(u + 1)
    if D.count(0) > 1:
        print(-1)
    else:
        print(1, *ans)
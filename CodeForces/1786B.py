for _ in range(int(input())):
    N, C_W, D_W = map(int, input().split())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    C_W *= 2
    D_W *= 2
    C_shift = C[0]
    for c in range(len(C)):
        C[c] -= C_shift

    D_shift = D[0]
    for d in range(len(D)):
        D[d] -= D_shift

    max_shift = C_W - D_W
    shift = 0
    for c, d in zip(C, D):
        max_shift = min(c + C_W - (d + D_W), max_shift)
        if d + shift < c:
            shift += c - (d + shift)
        if shift > max_shift or d+shift+D_W > c+C_W:
            print("NO")
            break
    else:
        print("YES")
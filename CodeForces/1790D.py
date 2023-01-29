for _ in range(int(input())):
    N = int(input())
    M = sorted(list(map(int, input().split())))
    quantity = {}
    sizes = []
    last = -1
    for m in M:
        if last != m:
            sizes.append(m)
            quantity[m] = 1
        else:
            quantity[m] += 1
        last = m
    ans = quantity[sizes[0]]
    for i in range(1, len(sizes)):
        if sizes[i-1] == sizes[i] - 1:
            ans += max(0, quantity[sizes[i]] - quantity[sizes[i-1]])
        else:
            ans += quantity[sizes[i]]
    print(ans) 
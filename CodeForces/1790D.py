for _ in range(int(input())):
    N = int(input())
    M = list(map(int, input().split()))
    quantity = {}
    for m in M:
        if m not in quantity:
            quantity[m] = 0
        quantity[m] += 1
    sizes = sorted(list(quantity.keys()))
    ans = quantity[sizes[0]]
    for i in range(1, len(sizes)):
        if sizes[i-1] == sizes[i] - 1:
            ans += max(0, quantity[sizes[i]] - quantity[sizes[i-1]])
        else:
            ans += quantity[sizes[i]]
    print(ans) 